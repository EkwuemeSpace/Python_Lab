import sys
from datetime import datetime

import pytest

from src.storage import load_expence, save_changes, generate_id
from src.utils import current_datetime, category_selector, date_input
from src.expenses import add_expence, view_expence, delete_expence
from src.search import search_expence
from src.reports import (
    total_expenditure,
    category_expenditure,
    monthly_summary,
    highest_expence,
)

SAMPLE = [
    {'id': 1, 'description': 'Lunch at market', 'category': 'Food',
     'amount': 1500, 'date': '2026-11-13'},
    {'id': 2, 'description': 'Bus fare to campus', 'category': 'Transportation',
     'amount': 700, 'date': '2026-10-20'},
    {'id': 3, 'description': 'Electricity bill', 'category': 'Utilities',
     'amount': 5000, 'date': '2026-11-02'},
]


# ---------- helpers ----------

@pytest.fixture
def data_file(tmp_path, monkeypatch):
    path = tmp_path / 'expenses.json'
    monkeypatch.setattr('src.storage.DATA_FILE', path)
    return path


@pytest.fixture
def filled_file(data_file):
    save_changes(data_file, SAMPLE)
    return data_file


def fake_inputs(monkeypatch, answers):
    answer_iter = iter(answers)
    monkeypatch.setattr('builtins.input', lambda prompt='': next(answer_iter))


# ---------- storage.py ----------

def test_load_missing_file_returns_empty_list(data_file):
    assert load_expence(data_file) == []


def test_load_broken_json_returns_empty_list(data_file):
    data_file.write_text('not json at all')
    assert load_expence(data_file) == []


def test_save_then_load_roundtrip(data_file):
    save_changes(data_file, SAMPLE)
    assert load_expence(data_file) == SAMPLE


def test_generate_id_empty_file_is_1(data_file):
    assert generate_id() == 1


def test_generate_id_is_highest_plus_one(filled_file):
    assert generate_id() == 4


# ---------- utils.py ----------

def test_current_datetime_has_date_and_time():
    result = current_datetime()
    assert set(result) == {'date', 'time'}
    datetime.strptime(result['date'], '%Y-%m-%d')
    datetime.strptime(result['time'], '%H:%M:%S')


@pytest.mark.parametrize('typed, expected', [
    ('1', 'Food'),
    ('7', 'Others'),
    ('0', None),
    ('8', None),
    ('abc', None),
    ('', None),
])
def test_category_selector(monkeypatch, typed, expected):
    fake_inputs(monkeypatch, [typed])
    assert category_selector() == expected


@pytest.mark.parametrize('typed, expected', [
    ('2026-11-13', '2026-11-13'),
    ('13/11/2026', None),
    ('2026-13-45', None),
    ('', None),
])
def test_date_input(monkeypatch, typed, expected):
    fake_inputs(monkeypatch, [typed])
    assert date_input('date: ') == expected


# ---------- expenses.py: add ----------

def test_add_expence_saves_valid_record(monkeypatch, data_file):
    fake_inputs(monkeypatch, ['Lunch at market', '1500', '1'])
    add_expence(data_file)

    records = load_expence(data_file)
    assert len(records) == 1
    assert records[0]['id'] == 1
    assert records[0]['description'] == 'Lunch at market'
    assert records[0]['category'] == 'Food'
    assert records[0]['amount'] == 1500
    datetime.strptime(records[0]['date'], '%Y-%m-%d')


@pytest.mark.parametrize('answers', [
    ['', '1500', '1'],                    # empty description
    ['Food', '1500', '1'],                # description too short
    ['Lunch at market', 'abc', '1'],      # amount not a number
    ['Lunch at market', '0', '1'],        # amount below 1
    ['Lunch at market', '1500', '9'],     # invalid category
])
def test_add_expence_rejects_bad_input(monkeypatch, data_file, answers):
    fake_inputs(monkeypatch, answers)
    add_expence(data_file)
    assert load_expence(data_file) == []


# ---------- expenses.py: view ----------

def test_view_empty(data_file, capsys):
    view_expence(data_file)
    assert 'No expenses found.' in capsys.readouterr().out


def test_view_shows_records_and_total(filled_file, capsys):
    view_expence(filled_file)
    out = capsys.readouterr().out
    assert 'Lunch at market' in out
    assert 'Electricity bill' in out
    assert 'Total records: 3' in out
    assert '7,200.00' in out


# ---------- expenses.py: delete ----------

def test_delete_empty(data_file, capsys):
    delete_expence(data_file)
    assert 'No expenses found.' in capsys.readouterr().out


def test_delete_confirmed_removes_record(monkeypatch, filled_file):
    fake_inputs(monkeypatch, ['1', 'y'])
    delete_expence(filled_file)
    ids = [e['id'] for e in load_expence(filled_file)]
    assert ids == [2, 3]


def test_delete_cancelled_keeps_everything(monkeypatch, filled_file):
    fake_inputs(monkeypatch, ['1', 'n'])
    delete_expence(filled_file)
    assert len(load_expence(filled_file)) == 3


@pytest.mark.parametrize('typed', ['0', '99', 'abc', ''])
def test_delete_bad_choice_keeps_everything(monkeypatch, filled_file, typed):
    fake_inputs(monkeypatch, [typed])
    delete_expence(filled_file)
    assert len(load_expence(filled_file)) == 3


# ---------- search.py ----------

def test_search_by_description(monkeypatch, filled_file, capsys):
    fake_inputs(monkeypatch, ['1', 'bus'])
    search_expence(filled_file)
    out = capsys.readouterr().out
    assert 'Bus fare to campus' in out
    assert 'Lunch at market' not in out
    assert 'Total matches: 1' in out


def test_search_by_category(monkeypatch, filled_file, capsys):
    fake_inputs(monkeypatch, ['2', '1'])
    search_expence(filled_file)
    out = capsys.readouterr().out
    assert 'Lunch at market' in out
    assert 'Bus fare to campus' not in out


def test_search_by_date_range(monkeypatch, filled_file, capsys):
    fake_inputs(monkeypatch, ['3', '2026-11-01', '2026-11-30'])
    search_expence(filled_file)
    out = capsys.readouterr().out
    assert 'Lunch at market' in out
    assert 'Electricity bill' in out
    assert 'Bus fare to campus' not in out
    assert 'Total matches: 2' in out


def test_search_end_before_start(monkeypatch, filled_file, capsys):
    fake_inputs(monkeypatch, ['3', '2026-11-30', '2026-11-01'])
    search_expence(filled_file)
    assert 'end date cannot be before start date' in capsys.readouterr().err


def test_search_no_match(monkeypatch, filled_file, capsys):
    fake_inputs(monkeypatch, ['1', 'zzz'])
    search_expence(filled_file)
    assert 'No matching expenses found.' in capsys.readouterr().out


def test_search_invalid_option(monkeypatch, filled_file, capsys):
    fake_inputs(monkeypatch, ['9'])
    search_expence(filled_file)
    assert 'invalid option' in capsys.readouterr().err


# ---------- reports.py ----------

def test_total_expenditure(filled_file, capsys):
    total_expenditure(filled_file)
    assert '7,200.00' in capsys.readouterr().out


def test_category_expenditure(monkeypatch, filled_file, capsys):
    fake_inputs(monkeypatch, ['1'])
    category_expenditure(filled_file)
    assert '1,500.00' in capsys.readouterr().out


def test_category_expenditure_no_records(monkeypatch, filled_file, capsys):
    fake_inputs(monkeypatch, ['4'])   # Education has no records
    category_expenditure(filled_file)
    assert 'No expenses found for Education.' in capsys.readouterr().out


def test_monthly_summary(filled_file, capsys):
    monthly_summary(filled_file)
    out = capsys.readouterr().out
    assert '2026-10' in out and '700.00' in out
    assert '2026-11' in out and '6,500.00' in out
    assert '90.3%' in out


def test_highest_expence(filled_file, capsys):
    highest_expence(filled_file)
    out = capsys.readouterr().out
    assert 'Electricity bill' in out
    assert '5,000.00' in out


@pytest.mark.parametrize('report', [
    total_expenditure, monthly_summary, highest_expence,
])
def test_reports_handle_empty_file(data_file, capsys, report):
    report(data_file)
    assert 'No expenses found.' in capsys.readouterr().out