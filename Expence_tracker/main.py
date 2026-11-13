from src import ui
from src.config import DATA_FILE
from src.expenses import add_expence, view_expence, delete_expence
from src.search import search_expence
from src.reports import (
    total_expenditure,
    category_expenditure,
    monthly_summary,
    highest_expence
)

MENU_ITEMS = [
    ('1', '➕ Add expense'),
    ('2', '📋 View expenses'),
    ('3', '🗑️  Delete expense'),
    ('4', '🔍 Search / filter expenses'),
    ('5', '💵 Total expenditure'),
    ('6', '📂 Category expenditure'),
    ('7', '📅 Monthly summary'),
    ('8', '🏆 Highest expense'),
    ('9', '🚪 Exit'),
]


def main():
    ui.banner()

    while True:
        ui.menu('Main Menu', MENU_ITEMS)
        user_input = ui.ask('choose an option:')

        if not user_input:
            ui.error('option cannot be empty!')
            continue

        if user_input == '1':
            add_expence(DATA_FILE)
        elif user_input == '2':
            view_expence(DATA_FILE)
        elif user_input == '3':
            delete_expence(DATA_FILE)
        elif user_input == '4':
            search_expence(DATA_FILE)
        elif user_input == '5':
            total_expenditure(DATA_FILE)
        elif user_input == '6':
            category_expenditure(DATA_FILE)
        elif user_input == '7':
            monthly_summary(DATA_FILE)
        elif user_input == '8':
            highest_expence(DATA_FILE)
        elif user_input == '9':
            ui.typewriter('Goodbye! 👋', style='bold green')
            break
        else:
            ui.error('invalid option!')
            continue

        ui.pause()
        ui.clear()


main()