# 💰 Expense Tracker

A colorful, menu-driven command-line expense tracker written in Python. Add, view, search, and delete expenses, and generate financial reports, all saved to a local JSON file.

## Features

- **Add expenses** with description, amount, and category (input is validated)
- **View expenses** in a styled table with a running total
- **Delete expenses** with a confirmation step before anything is removed
- **Search and filter** by description keyword, category, or date range
- **Financial reports:**
  - Total expenditure
  - Expenditure for a selected category
  - Monthly summary with each month's share of the total
  - Highest individual expense
- **Colorful terminal UI** with animated spinner, progress bar, and typewriter banner (powered by [rich](https://github.com/Textualize/rich))
- **Automated tests** with pytest (45 tests)

## Categories

Food, Transportation, Utilities, Education, Healthcare, Entertainment, Others

## Project Structure

```
Expence_tracker/
├── main.py              # Entry point and main menu loop
├── README.md
├── requirements.txt
├── data/
│   └── expenses.json    # Saved expenses (created automatically)
├── src/
│   ├── __init__.py
│   ├── config.py        # Paths and settings
│   ├── storage.py       # Load / save JSON, generate IDs
│   ├── utils.py         # Date helper, category selector, date input
│   ├── ui.py            # All colors, animations, tables, and prompts
│   ├── expenses.py      # Add, view, delete
│   ├── search.py        # Search and filtering
│   └── reports.py       # Financial reports
└── tests/
    └── test_all.py      # pytest test suite
```

## Requirements

- Python 3.10 or newer
- `rich`
- `pytest` (only needed to run the tests)

## Installation

```bash
git clone https://github.com/EkwuemeSpace/Python_Lab.git
cd Expence_tracker

python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate

pip install rich pytest
```

## Usage

Run from the project root:

```bash
python3 main.py
```

### Menu

| Option | Action |
|---|---|
| 1 | Add expense |
| 2 | View expenses |
| 3 | Delete expense |
| 4 | Search / filter expenses |
| 5 | Total expenditure |
| 6 | Category expenditure |
| 7 | Monthly summary |
| 8 | Highest expense |
| 9 | Exit |

### Adding an expense

1. Enter a description (more than 5 characters)
2. Enter an amount (whole number, at least 1)
3. Pick a category by number

The date is recorded automatically.

### Searching

- **By description:** matches any expense containing your keyword (not case sensitive)
- **By category:** pick from the category list
- **By date range:** enter a start and end date in `YYYY-MM-DD` format. For a single day, use the same date for both.

## Data Format

Expenses are stored in `data/expenses.json` as a list:

```json
[
    {
        "id": 1,
        "description": "Lunch at the market",
        "category": "Food",
        "amount": 1500,
        "date": "2026-11-13"
    }
]
```

Dates use `YYYY-MM-DD`, which sorts correctly as text. That is what makes date-range filtering and monthly summaries simple.

## Running the Tests

```bash
python3 -m pytest -v
```

Tests use temporary files, so your real `expenses.json` is never touched. Animations are skipped automatically when output is not a real terminal, so they don't interfere with tests.

## Design Notes

- **One file owns the look.** Only `src/ui.py` imports `rich`, so restyling the app means editing one file.
- **Validate first, return early.** Each function checks its input and exits with a clear error before doing any work.
- **Errors go to stderr.** This keeps error messages separate from normal output and makes them testable.

## Known Limitations

- If two expenses tie for the highest amount, only the first is shown
- `generate_id()` reads the default data file rather than the path passed to the other functions
- Amounts are whole numbers only (no decimals)
- Records saved in an older date format (for example `13-Nov-2026`) must be deleted or converted

## Ideas for Next Steps

- Edit an existing expense
- Export to CSV
- Decimal amounts
- Set a monthly budget with warnings

## Author

Innocent Ekwueme ([Innocent_Go_Dev](https://github.com/Innocent_Go_Dev))