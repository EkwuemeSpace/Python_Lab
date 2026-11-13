from src import ui
from src.storage import load_expence
from src.utils import category_selector, date_input


def search_expence(file_path):
    expences = load_expence(file_path)

    if not expences:
        ui.warning('No expenses found.')
        return

    ui.menu('Search / Filter', [
        ('1', 'Search by description'),
        ('2', 'Filter by category'),
        ('3', 'Filter by date range'),
    ])

    user_input = ui.ask('choose an option:')
    results = []

    if user_input == '1':
        keyword = ui.ask('Enter a keyword:').lower()
        if not keyword:
            ui.error('keyword cannot be empty!')
            return
        for expence in expences:
            if keyword in expence['description'].lower():
                results.append(expence)

    elif user_input == '2':
        category = category_selector()
        if not category:
            return
        for expence in expences:
            if expence['category'] == category:
                results.append(expence)

    elif user_input == '3':
        start = date_input('Enter start date (YYYY-MM-DD):')
        if not start:
            return
        end = date_input('Enter end date (YYYY-MM-DD):')
        if not end:
            return
        if end < start:
            ui.error('end date cannot be before start date!')
            return
        for expence in expences:
            if start <= expence['date'] <= end:
                results.append(expence)

    else:
        ui.error('invalid option!')
        return

    if not results:
        ui.warning('No matching expenses found.')
        return

    ui.expense_table(results, 'Results')
    ui.info(f'Total matches: {len(results)}')