from pathlib import Path
import json
import sys

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR / "data" / "tasks.json"
DATA_FILE.parent.mkdir(parents=True, exist_ok=True)

def id_generator():
    save_content = task_loader(DATA_FILE)

    task_id = 0
    for task in save_content:
        if task['id'] > task_id:
            task_id = task['id']
    return task_id + 1



def task_loader(file_path):
    try:
        with file_path.open('r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_task(file_path, task):
    with file_path.open('w', encoding='utf-8') as f:
        json.dump(task, f, indent=4)


def add_task(file_path):
    task_title = input('please enter task title: ').strip()

    if not task_title:
        print('error: task name cannot be empty!', file=sys.stderr)
        return
    
    if len(task_title) <= 5:
        print('error: task name is unreasonable', file=sys.stderr)
        return

    new_task = {
        'id': id_generator(),
        'title': task_title,
        'done': False
    }

    loaded_content = task_loader(file_path)
    loaded_content.append(new_task)
    save_task(file_path, loaded_content)
    print('Task added successfully!')
    return

def update_task(file_path):
    loaded_content = task_loader(file_path)

    try:
        task_id = int(input('enter task id: ').strip())
        if not task_id:
            print('error: task_id cannot be empty', file=sys.stderr)
            return
    except ValueError:
        print('task_id must be an integer', file=sys.stderr)
        return


    for task in loaded_content:
        if task['id'] == task_id:
            view_tasks(file_path)
            task['done'] = True
            print('Task updated successfully')
            save_task(file_path, loaded_content)
            return
    print(f'Task id: {task_id} not found!', file=sys.stderr)


def delete_task(file_path):
    try:
        task_id = int(input('enter task id: ').strip())
        if not task_id:
            print('error: task id cannot be empty!', file=sys.stderr)
            return
    except ValueError:
        print('task id must be an integer', file=sys.stderr)
        return

    loaded_content = task_loader(file_path)

    for index, task in enumerate(loaded_content):
        if task['id'] == task_id:
            loaded_content.pop(index)
            save_task(file_path, loaded_content)
            print('Task deleted successfully')
            return
    print(f'Task id: {task_id} not found!')


def view_tasks(file_path):
    tasks = task_loader(file_path)

    if not tasks:
        print("\nNo tasks available. Add a task to get started!")
        return

    print("\n" + "=" * 55)
    print("                 YOUR TASK KEEPER")
    print("=" * 55)

    for task in tasks:
        status = "✓ Completed" if task["done"] else "○ Pending"

        print(f"""
    Task ID : {task['id']}
    Title   : {task['title']}
    Status  : {status}
    {"-" * 45}""")

    print("=" * 55)
    print(f"Total tasks: {len(tasks)}")
