# Task Keeper CLI V2

Task Keeper is a command-line task management application built with Python. It helps users organise their daily responsibilities by allowing them to create, view, complete, and delete tasks directly from the terminal.

This is the second version of the project. It builds on my previous CLI task manager, with improvements to the user experience, code organisation, task handling, and terminal interface.

## Features

- **Add Tasks:** Create new tasks with automatically generated IDs.
- **View Tasks:** Display all saved tasks, including their IDs, titles, and completion status.
- **Complete Tasks:** Mark existing tasks as completed.
- **Delete Tasks:** Remove tasks that are no longer needed.
- **Persistent Storage:** Save tasks in a JSON file so they remain available after closing the application.
- **Animated Terminal Interface:** Display an interactive welcome screen and animated task information with terminal colours.
- **Input Validation:** Handle invalid inputs and prevent certain incorrect operations.

## Technologies Used

- Python
- JSON
- pathlib
- sys
- time

## Project Structure

```text
task_keeper/
│
├── data/
│   └── tasks.json
│
├── package/
│   ├── __init__.py
│   ├── storage.py
│   ├── utils.py
│   └── helpers.py
│
├── main.py
└── README.md
```

The project structure may vary slightly depending on the local setup.

## Getting Started

### 1. Clone the Repository

```bash
git clone <repository-url>
```

### 2. Navigate into the Project Directory

```bash
cd task_keeper
```

### 3. Run the Application

```bash
python3 main.py
```

No external Python packages are required for the application's core functionality.

## How to Use

When the application starts, it displays a welcome screen with the available operations.

| Option | Operation | Description |
|---|---|---|
| 1 | Add Task | Create a new task |
| 2 | View Tasks | Display all saved tasks |
| 3 | Complete Task | Mark a task as completed |
| 4 | Delete Task | Remove a task |
| 5 | Exit | Close the application |

Follow the terminal prompts to perform an operation.

## Data Storage

Task Keeper uses JSON for local data storage. Tasks are stored as a list of dictionaries, with each task containing an ID, title, and completion status.

Example:

```json
[
    {
        "id": 1,
        "title": "Learn Python file handling",
        "done": false
    },
    {
        "id": 2,
        "title": "Build a CLI application",
        "done": true
    }
]
```

This allows tasks to remain saved between application sessions.

## What I Improved in V2

Compared with my previous CLI task manager, this version focuses on improving both functionality and presentation.

- Improved the terminal interface with colours and text animations.
- Added a more structured project organisation.
- Improved task creation, retrieval, completion, and deletion workflows.
- Strengthened input validation and error handling.
- Used JSON-based persistence to retain task records.

## What I Learned

Working on this version helped me practise and strengthen my understanding of:

- Python functions and modular programming.
- Reading from and writing to JSON files.
- Working with lists and dictionaries.
- File paths and directory management.
- Exception handling and input validation.
- Loops and conditional logic.
- Building interactive command-line applications.
- Improving the user experience through terminal formatting and animation.

## Future Improvements

Some features I would like to explore in future versions include:

- Task priority levels.
- Task deadlines and reminders.
- Searching and filtering tasks.
- Editing existing tasks.
- Unit testing.
- A database-backed storage option.

## Author

**Innocent Ekwueme**

Aspiring Software Engineer

GitHub: [EkwuemeSpace](https://github.com/EkwuemeSpace)

---

Task Keeper CLI V2 is a practical project focused on strengthening my Python programming skills through building, improving, and maintaining a functional command-line application.