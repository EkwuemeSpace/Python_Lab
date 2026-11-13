from datetime import datetime

from src import ui


def current_datetime():
    now = datetime.now()
    return {
        'date': now.strftime('%Y-%m-%d'),
        'time': now.strftime('%H:%M:%S')
    }


def category_selector():
    valid_category = (
        'Food',
        'Transportation',
        'Utilities',
        'Education',
        'Healthcare',
        'Entertainment',
        'Others'
    )

    ui.menu('Categories', [(str(i), cat) for i, cat in enumerate(valid_category, 1)])

    try:
        user_input = ui.ask('choose a category:')
        if not user_input:
            ui.error('category cannot be empty')
            return
        user_choice = int(user_input)
        num = list(range(1, len(valid_category) + 1))
        if user_choice not in num:
            ui.error('invalid choice detected!')
            return
        return valid_category[user_choice - 1]
    except ValueError as e:
        ui.error(str(e))
        return


def date_input(prompt):
    user_input = ui.ask(prompt)
    if not user_input:
        ui.error('date cannot be empty!')
        return
    try:
        datetime.strptime(user_input, '%Y-%m-%d')
    except ValueError:
        ui.error('invalid date, use YYYY-MM-DD (e.g. 2026-11-13)')
        return
    return user_input