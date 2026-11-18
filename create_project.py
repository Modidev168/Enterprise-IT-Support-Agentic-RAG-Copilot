from pathlib import Path

# Current Working Directory

root = Path(".")

# Folders to create
folders = [
    "app/api",
    "app/core",
    "app/rag",
    "app/services",
    "data",
    "templates",
    "static",
    "uploads",
    "tests"
]

# Files To Create
files = [
    "requirements.txt",
    "app/main.py",
    "ingest_sample_kb.py",
    "run.py",
    ".env",
]

for folder in folders:
    (root / folder).mkdir(parents=True,exist_ok=True)

for file in files:
    (root / file).touch(exist_ok=True)


print("Project's Files and Folder Created Successfully.")