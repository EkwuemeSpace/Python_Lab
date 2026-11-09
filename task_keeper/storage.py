from pathlib import Path
import json

location = Path(__file__).absolute().parent
file_path = location / 'data' / 'tasks.json'


#load task function
def load_task(path):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            text = f.read()
    except FileNotFoundError:
        return []

    if not text.strip():
        return []

    return json.loads(text)


#id generator
def generate_id(tasks):
    highest_id = 0

    for task in tasks:
        if task['id'] > highest_id:
            highest_id = task['id']
        
    return highest_id + 1

def validate_tasks(tasks: list) -> None:
    required_keys = ['id', 'title', 'completed']

    if not isinstance(tasks, list):
        raise ValueError('error: expected list!')
    
    for task in tasks:
        if not isinstance(task, dict):
            raise ValueError('error: expected dict')
        
        for key in required_keys:
            if key not in task:
                raise ValueError(f'error: missing required key: {key}')

#path and a list. It makes sure the folder exists, then writes the list. It asks the user         
def write_tasks(path, tasks):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(tasks, f, indent=2)

#save task function
def save_task(path):
    path = Path(path)

    #collected task title
    title = input('Enter a task title: ').strip()
    if not title:
        print('error: Title cannot be empty!')
        return
    
    tasks = load_task(path)
    new_task = {
        'id': generate_id(tasks),
        'title': title,
        'completed': False
    }
    tasks.append(new_task)

    path.parent.mkdir(parents=True, exist_ok=True)
    write_tasks(path, tasks)
    print('TASK SAVED SUCCESSFULLY!!')


def update_task_status(path):
    path = Path(path)
    
    try:
        task_id = int(input('Enter task id: ').strip())
    except ValueError:
        print('task id must be an integer!')
        return

    loaded_task = load_task(path)
    found = False

    for task in loaded_task:
        if task['id'] == task_id:
            found = True
            task['completed'] = True
            break
    if not found:
        print('task id not found!')
    else:
        write_tasks(path, loaded_task)
        print('status updated successfully!')
    

#delete task function
def delete_task(path):
    path = Path(path)
    found = False
    try:
        task_id = int(input('enter task id: ').strip())
    except ValueError:
        print('id must be an integer')
        return
    
    loaded_task = load_task(path)

    for task in loaded_task:
        if task['id'] == task_id:
            found = True
            loaded_task.remove(task)
            break

    if not found:
        print('Task id not found!')
        return
    
    write_tasks(path, loaded_task)
    print('Task deleted successfully')
    