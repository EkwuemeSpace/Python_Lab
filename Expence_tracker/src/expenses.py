from src import ui
from src.storage import load_expence, save_changes, generate_id
from src.utils import category_selector, current_datetime


def add_expence(file_path):
    try:
        expence_description = ui.ask('Enter expence description:')
        if not expence_description:
            ui.error('expence description cannot be empty')
            return
        if len(expence_description) <= 5:
            ui.error('Expense description is not meaningful.')
            return
    except ValueError as e:
        ui.error(str(e))
        return

    try:
        amount = int(ui.ask('Enter amount:'))
        if amount < 1:
            ui.error('amount must be greater than 0')
            return
    except ValueError as e:
        ui.error(str(e))
        return

    category = category_selector()
    if not category:
        return

    my_expence = {
        'id': generate_id(),
        'description': expence_description,
        'category': category,
        'amount': amount,
        'date': current_datetime()['date']
    }

    loader = load_expence(file_path)
    loader.append(my_expence)

    with ui.spinner('Saving expense...'):
        save_changes(file_path, loader)
    ui.success('Expense saved!')


def view_expence(file_path):
    loader = load_expence(file_path)

    if not loader:
        ui.warning('No expenses found.')
        return

    ui.expense_table(loader, 'Expenses')

    total = 0
    for expence in loader:
        total += expence['amount']
    ui.info(f'Total records: {len(loader)}')
    ui.info(f'Total amount: {total:,.2f}')


def delete_expence(file_path):
    expences = load_expence(file_path)

    if not expences:
        ui.warning('No expenses found.')
        return

    ui.expense_table(expences, 'Delete which expense?')

    try:
        user_input = ui.ask('Enter the number of the expense to delete:')
        if not user_input:
            ui.error('choice cannot be empty!')
            return
        user_choice = int(user_input)
        if user_choice not in range(1, len(expences) + 1):
            ui.error('expense not found!')
            return
    except ValueError as e:
        ui.error(str(e))
        return

    target = expences[user_choice - 1]
    if not ui.confirm(
        f"Delete '{target['description']}' ({target['amount']:,.2f})? This cannot be undone"
    ):
        ui.warning('Deletion cancelled.')
        return

    expences.pop(user_choice - 1)
    with ui.spinner('Deleting expense...'):
        save_changes(file_path, expences)
    ui.success('Expense deleted.')