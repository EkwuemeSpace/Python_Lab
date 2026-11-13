from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR / "data" / "tasks.json"
DATA_FILE.parent.mkdir(parents=True, exist_ok=True)