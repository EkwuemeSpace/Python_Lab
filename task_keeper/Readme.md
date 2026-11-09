# Task Keeper

A command-line task manager written in Python. Add, view, complete and delete tasks from an interactive, colorful terminal menu. Tasks are saved to a local JSON file, so they persist between runs.

## Features

- **Add** tasks with a title (empty titles are rejected)
- **View** all tasks in a table with done/pending status and a progress count
- **Complete** a task by its id
- **Delete** a task by its id
- **Persistent storage** in `data/tasks.json`, created automatically on first save
- **Safe handling** of a missing file, a missing `data` folder, an empty file, and invalid input
- **Terminal polish:** ANSI colors, loading bar, spinner and typewriter effects (standard library only)

## Requirements

- Python 3.8 or newer
- A terminal that supports ANSI colors (most Linux and macOS terminals, Windows Terminal)

No third-party packages are needed.

## Getting Started

```bash
git clone https://github.com/EkwuemeSpace/Python_Lab.git
cd task_keeper
python3 main.py
```

## Usage

```
What would you like to do?
  1  Add task
  2  View tasks
  3  Complete task
  4  Delete task
  5  Quit
```

Example view:

```
  ID   STATUS      TITLE
  ─────────────────────────────────
  1    ✔ done      Buy milk
  2    ○ pending   Write code
  ─────────────────────────────────
  1 done / 2 total
```

## Project Structure

```
task_keeper/
├── main.py      # Menu, user interaction, colors and animations
├── storage.py   # Task logic and reading/writing data/tasks.json
├── data/
│   └── tasks.json   # Created automatically on first save
└── README.md
```

## Data Format

Tasks are stored as a JSON list of objects:

```json
[
  {
    "id": 1,
    "title": "Buy milk",
    "completed": false
  }
]
```

Ids are generated automatically as the highest existing id plus one.

## Error Handling

| Situation | Behavior |
|-----------|----------|
| `tasks.json` or `data/` missing | Treated as an empty list; folder and file are created on save |
| `tasks.json` empty | Treated as an empty list |
| Empty task title | Rejected with a message |
| Non-numeric task id | Rejected with a message |
| Task id not found | Reports "not found"; nothing is changed |
| Ctrl+C | Exits cleanly |

## Roadmap

- Separate user interaction from data logic into distinct modules
- Handle corrupted (non-empty, invalid) JSON with a friendly message
- Edit task titles
- Unit tests with `pytest`

## Author

Built by Innocent Ekwueme ([@Innocent_Go_Dev](https://github.com/Innocent_Go_Dev)) as part of a Python learning journey.