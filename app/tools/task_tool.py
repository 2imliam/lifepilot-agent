import json
from pathlib import Path

DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "tasks.json"


def _load_tasks():
    if not DATA_PATH.exists():
        return []
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def _save_tasks(tasks):
    with open(DATA_PATH, "w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False, indent=2)


def list_tasks():
    """List all personal tasks."""
    return _load_tasks()


def add_task(title: str, deadline: str = "", priority: str = "medium"):
    """Add a new personal task."""
    tasks = _load_tasks()
    new_id = max([task["id"] for task in tasks], default=0) + 1

    task = {
        "id": new_id,
        "title": title,
        "deadline": deadline,
        "priority": priority,
        "status": "pending"
    }

    tasks.append(task)
    _save_tasks(tasks)
    return task


def update_task_status(task_id: int, status: str):
    """Update task status."""
    tasks = _load_tasks()

    for task in tasks:
        if task["id"] == task_id:
            task["status"] = status
            _save_tasks(tasks)
            return task

    return {"error": "Task not found"}