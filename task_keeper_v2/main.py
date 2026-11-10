
import sys

from package.utils import welcome, goodbye
from package.storage import (
    task_loader,
    add_task,
    view_tasks,
    update_task,
    delete_task,
    DATA_FILE
)


def main():
    welcome()

    task_loader(DATA_FILE)

    valid_operation = ('1', '2', '3', '4', '5')
    while True:
        interactor = input('Choose an operation: ').strip()

        if not interactor:
            print('Error: input cannot be empty!', file=sys.stderr)
            continue

        if interactor not in valid_operation:
            print('Error: you have entered an invalid operation!')
            continue

        if interactor == '1':
            add_task(DATA_FILE)

        elif interactor == '2':
            view_tasks(DATA_FILE)

        elif interactor == '3':
            update_task(DATA_FILE)

        elif interactor == '4':
            delete_task(DATA_FILE)

        elif interactor == '5':
            goodbye()
            break


if __name__ == "__main__":
    main()
