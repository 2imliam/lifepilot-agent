import json
from pathlib import Path

DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "notes.json"


def _load_notes():
    if not DATA_PATH.exists():
        return []
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def read_notes():
    """Read all personal notes."""
    return _load_notes()


def summarize_notes_basic(note_id: int):
    """Basic note summary for demo."""
    notes = _load_notes()

    for note in notes:
        if note["id"] == note_id:
            content = note["content"]

            return {
                "title": note["title"],
                "summary": content[:250] + "...",
                "action_items": [
                    "Build ADK personal assistant agent",
                    "Create web UI",
                    "Write README",
                    "Prepare evaluation cases",
                    "Record demo video"
                ]
            }

    return {"error": "Note not found"}