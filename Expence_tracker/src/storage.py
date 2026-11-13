import json
from src.config import DATA_FILE

def load_expence(file_path):
    try:
        with file_path.open('r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []
    

def generate_id():
    save_content = load_expence(DATA_FILE)

    task_id = 0
    for task in save_content:
        if task['id'] > task_id:
            task_id = task['id']
    return task_id + 1

    
def save_changes(file_path, task):
    with file_path.open('w', encoding='utf-8') as f:
        json.dump(task, f, indent=4)