import json
from pathlib import Path
from datetime import datetime
import streamlit as st

# =========================
# Paths
# =========================
PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "app" / "data"

TASKS_PATH = DATA_DIR / "tasks.json"
CALENDAR_PATH = DATA_DIR / "calendar.json"
NOTES_PATH = DATA_DIR / "notes.json"


# =========================
# Helpers
# =========================
def load_json(path, default):
    if not path.exists():
        return default
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def load_tasks():
    return load_json(TASKS_PATH, [])


def load_calendar():
    return load_json(CALENDAR_PATH, [])


def load_notes():
    return load_json(NOTES_PATH, [])


def create_daily_plan(tasks):
    if not tasks:
        return "No tasks found. Please add tasks to app/data/tasks.json."

    high = [t for t in tasks if t.get("priority") == "high"]
    medium = [t for t in tasks if t.get("priority") == "medium"]
    low = [t for t in tasks if t.get("priority") == "low"]

    ordered_tasks = high + medium + low

    time_blocks = [
        "08:00 - 09:30",
        "09:45 - 11:30",
        "14:00 - 16:00",
        "17:30 - 19:00",
        "20:00 - 21:30",
    ]

    lines = ["### Today Plan"]
    for i, task in enumerate(ordered_tasks):
        block = time_blocks[i] if i < len(time_blocks) else "Flexible time"
        lines.append(
            f"- **{block}**: {task.get('title')} "
            f"({task.get('priority', 'medium')} priority)"
        )

    lines.append("\n**Safety note:** No reminders were created automatically.")
    return "\n".join(lines)


def create_priority_text(tasks):
    if not tasks:
        return "No tasks found."

    priority_order = {"high": 1, "medium": 2, "low": 3}
    sorted_tasks = sorted(
        tasks,
        key=lambda t: priority_order.get(t.get("priority", "medium"), 2)
    )

    lines = ["### Task Priority"]
    for idx, task in enumerate(sorted_tasks, start=1):
        lines.append(
            f"{idx}. **{task.get('title')}** "
            f"- Priority: `{task.get('priority', 'medium')}` "
            f"- Deadline: {task.get('deadline', 'No deadline')}"
        )

    return "\n".join(lines)


def summarize_notes(notes):
    if not notes:
        return "No notes found."

    note = notes[0]
    content = note.get("content", "")

    return f"""
### Notes Summary

**Title:** {note.get("title", "Untitled")}

**Summary:**  
{content[:300]}...

**Action items:**
- Build ADK personal assistant agent
- Create web UI
- Add evaluation cases
- Prepare README
- Record demo video
"""


def mock_agent_response(user_message):
    msg = user_message.lower()

    tasks = load_tasks()
    notes = load_notes()

    if "plan" in msg or "schedule" in msg or "day" in msg:
        return create_daily_plan(tasks)

    if "priority" in msg or "first" in msg or "ưu tiên" in msg:
        return create_priority_text(tasks)

    if "summarize" in msg or "summary" in msg or "tóm tắt" in msg:
        return summarize_notes(notes)

    if "remind" in msg or "nhắc" in msg:
        draft = {
            "content": user_message,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "status": "draft",
            "requires_confirmation": True,
        }
        st.session_state.reminder_drafts.append(draft)
        st.session_state.safety_logs.append(
            "Created reminder draft. User confirmation is required before saving."
        )

        return """
### Reminder Draft Created

I created a reminder draft based on your request.

**Status:** Draft  
**Requires confirmation:** Yes  

I will not save or send this reminder until you confirm.
"""

    return """
I am LifePilot AI, your privacy-first personal assistant.

You can ask me to:
- Plan your day
- Prioritize tasks
- Summarize notes
- Draft reminders safely
"""


# =========================
# Streamlit setup
# =========================
st.set_page_config(
    page_title="LifePilot AI",
    page_icon="🧭",
    layout="wide"
)

if "messages" not in st.session_state:
    st.session_state.messages = []

if "reminder_drafts" not in st.session_state:
    st.session_state.reminder_drafts = []

if "safety_logs" not in st.session_state:
    st.session_state.safety_logs = [
        "Mock mode enabled: No Gemini API calls.",
        "All demo data is loaded from local JSON files.",
        "Write actions require confirmation."
    ]


# =========================
# Header
# =========================
st.title("🧭 LifePilot AI")
st.caption("Privacy-first Personal Assistant — Mock Demo Mode")

st.info(
    "This demo does not call Gemini or external APIs. "
    "It uses local JSON data and simple mock agent logic for project demonstration."
)


# =========================
# Load data
# =========================
tasks = load_tasks()
calendar = load_calendar()
notes = load_notes()


# =========================
# Main layout
# =========================
left, right = st.columns([1.2, 1])


with left:
    st.subheader("💬 Chat with LifePilot")

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    user_input = st.chat_input("Ask LifePilot to plan, prioritize, summarize, or remind...")

    if user_input:
        st.session_state.messages.append(
            {"role": "user", "content": user_input}
        )

        response = mock_agent_response(user_input)

        st.session_state.messages.append(
            {"role": "assistant", "content": response}
        )

        st.rerun()


with right:
    st.subheader("📌 Quick Actions")

    if st.button("Generate Today Plan"):
        response = create_daily_plan(tasks)
        st.session_state.messages.append(
            {"role": "assistant", "content": response}
        )
        st.rerun()

    if st.button("Show Task Priority"):
        response = create_priority_text(tasks)
        st.session_state.messages.append(
            {"role": "assistant", "content": response}
        )
        st.rerun()

    if st.button("Summarize Notes"):
        response = summarize_notes(notes)
        st.session_state.messages.append(
            {"role": "assistant", "content": response}
        )
        st.rerun()


# =========================
# Dashboard sections
# =========================
st.divider()

tab1, tab2, tab3, tab4, tab5 = st.tabs(
    ["Today Plan", "Tasks", "Notes", "Reminder Drafts", "Safety Log"]
)


with tab1:
    st.subheader("🗓️ Today Plan")
    st.markdown(create_daily_plan(tasks))


with tab2:
    st.subheader("✅ Task Priority Table")

    if tasks:
        st.dataframe(tasks, use_container_width=True)
    else:
        st.warning("No tasks found.")


with tab3:
    st.subheader("📝 Notes Summary")

    if notes:
        st.markdown(summarize_notes(notes))
    else:
        st.warning("No notes found.")


with tab4:
    st.subheader("⏰ Reminder Drafts")

    if st.session_state.reminder_drafts:
        for idx, draft in enumerate(st.session_state.reminder_drafts, start=1):
            st.write(f"### Draft {idx}")
            st.json(draft)

            if draft.get("status") == "draft":
                if st.button(f"Confirm Draft {idx}", key=f"confirm_{idx}"):
                    draft["status"] = "confirmed"
                    draft["requires_confirmation"] = False
                    st.session_state.safety_logs.append(
                        f"User confirmed reminder draft {idx}."
                    )
                    st.success(f"Draft {idx} confirmed.")
                    st.rerun()
    else:
        st.info("No reminder drafts yet.")


with tab5:
    st.subheader("🛡️ Privacy & Safety Log")

    for log in st.session_state.safety_logs:
        st.write(f"- {log}")