from src import ui
from src.storage import load_expence
from src.utils import category_selector


def total_expenditure(file_path):
    expences = load_expence(file_path)

    if not expences:
        ui.warning('No expenses found.')
        return

    total = 0
    for expence in expences:
        total += expence['amount']

    ui.progress('Calculating total...')
    ui.report_panel('TOTAL EXPENDITURE', [
        ('Records', len(expences)),
        ('Total spent', f'{total:,.2f}'),
    ])


def category_expenditure(file_path):
    expences = load_expence(file_path)

    if not expences:
        ui.warning('No expenses found.')
        return

    category = category_selector()
    if not category:
        return

    total = 0
    count = 0
    for expence in expences:
        if expence['category'] == category:
            total += expence['amount']
            count += 1

    if count == 0:
        ui.warning(f'No expenses found for {category}.')
        return

    ui.progress(f'Calculating {category}...')
    ui.report_panel(f'CATEGORY: {category.upper()}', [
        ('Records', count),
        ('Total spent', f'{total:,.2f}'),
    ])


def monthly_summary(file_path):
    expences = load_expence(file_path)

    if not expences:
        ui.warning('No expenses found.')
        return

    months = {}
    for expence in expences:
        month = expence['date'][:7]
        months[month] = months.get(month, 0) + expence['amount']

    grand_total = sum(months.values())

    rows = []
    for month in sorted(months):
        share = months[month] / grand_total * 100
        rows.append((month, f'{share:.1f}%', f'{months[month]:,.2f}'))
    rows.append(('[bold]Total[/bold]', '', f'[bold]{grand_total:,.2f}[/bold]'))

    ui.progress('Building summary...')
    ui.table_report('MONTHLY SUMMARY', ['Month', 'Share', 'Amount'], rows)


def highest_expence(file_path):
    expences = load_expence(file_path)

    if not expences:
        ui.warning('No expenses found.')
        return

    highest = expences[0]
    for expence in expences:
        if expence['amount'] > highest['amount']:
            highest = expence

    ui.progress('Searching...')
    ui.report_panel('HIGHEST EXPENSE', [
        ('Description', highest['description']),
        ('Category', highest['category']),
        ('Date', highest['date']),
        ('Amount', f"{highest['amount']:,.2f}"),
    ])