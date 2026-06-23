from pathlib import Path
import sys

# Allow imports from project root
PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(PROJECT_ROOT))

from app.tools.task_tool import list_tasks
from app.tools.calendar_tool import check_free_time
from app.tools.notes_tool import read_notes, summarize_notes_basic
from app.tools.reminder_tool import create_reminder_draft


def check(test_name, condition):
    if condition:
        print(f"PASS: {test_name}")
    else:
        print(f"FAIL: {test_name}")


def run_evals():
    print("Running LifePilot local evaluation suite...\n")

    # Test 1: Tasks
    tasks = list_tasks()
    check("list_tasks returns a list", isinstance(tasks, list))
    check("list_tasks has at least one task", len(tasks) > 0)

    # Test 2: Calendar / free time
    free_time = check_free_time()
    check("check_free_time returns a dictionary", isinstance(free_time, dict))
    check(
        "check_free_time includes suggested free blocks",
        "suggested_free_blocks" in free_time
    )

    # Test 3: Notes
    notes = read_notes()
    check("read_notes returns a list", isinstance(notes, list))
    check("read_notes has at least one note", len(notes) > 0)

    summary = summarize_notes_basic(1)
    check("summarize_notes_basic returns a dictionary", isinstance(summary, dict))
    check("summary includes action items", "action_items" in summary)

    # Test 4: Reminder safety
    reminder = create_reminder_draft(
        content="Submit Kaggle project",
        reminder_time="2026-07-05 21:00"
    )

    draft = reminder.get("draft", {})
    check("create_reminder_draft returns draft", isinstance(draft, dict))
    check("reminder status is draft", draft.get("status") == "draft")
    check(
        "reminder requires confirmation",
        draft.get("requires_confirmation") is True
    )

    print("\nEvaluation completed.")


if __name__ == "__main__":
    run_evals()