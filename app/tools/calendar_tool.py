import json
from pathlib import Path

DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "calendar.json"


def _load_calendar():
    if not DATA_PATH.exists():
        return []
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def get_today_calendar(date: str = "2026-07-04"):
    """Get calendar events for a specific date."""
    events = _load_calendar()
    return [event for event in events if event["date"] == date]


def check_free_time(date: str = "2026-07-04"):
    """Return simple available time blocks for demo."""
    busy_events = get_today_calendar(date)

    return {
        "date": date,
        "busy_events": busy_events,
        "suggested_free_blocks": [
            "09:45 - 11:30",
            "11:30 - 13:30",
            "17:30 - 20:30",
            "21:00 - 22:30"
        ]
    }