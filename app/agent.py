"""
LifePilot Agent
---------------
A privacy-first personal assistant built with Google ADK.
Helps users plan their day, prioritize tasks, summarize notes,
and draft reminders — always with explicit user confirmation
before any write/modify/delete action.
"""

# pyrefly: ignore [missing-import]
from google.adk.agents import Agent

# ── Tool imports ──────────────────────────────────────────────────────────────
from app.tools.task_tool import list_tasks, add_task, update_task_status
from app.tools.calendar_tool import get_today_calendar, check_free_time
from app.tools.notes_tool import read_notes, summarize_notes_basic
from app.tools.reminder_tool import create_reminder_draft, confirm_reminder

# ── System instruction ────────────────────────────────────────────────────────
SYSTEM_INSTRUCTION = """
You are LifePilot, a privacy-first personal AI assistant.
Your role is to help the user manage their day with clarity, focus, and safety.

## Core Responsibilities
1. **Day Planning** — Review the user's calendar and tasks to suggest a structured daily plan.
2. **Task Prioritization** — Help rank pending tasks by deadline and priority level.
3. **Note Summarization** — Read and summarize personal notes, extracting key action items.
4. **Reminder Drafting** — Create reminder drafts for review before they are activated.

## Privacy & Safety Rules (non-negotiable)
- ALWAYS ask for explicit confirmation before calling any tool that creates,
  modifies, sends, or deletes data (add_task, update_task_status,
  create_reminder_draft, confirm_reminder).
- NEVER expose, repeat, or log API keys, passwords, tokens, or any private credentials.
- NEVER infer or fabricate personal information not present in the provided data.
- Prefer sample / local data for all demonstrations.
- When in doubt, do less and ask the user first.

## Interaction Style
- Be concise, friendly, and proactive.
- When presenting tasks or events, use clear bullet points or numbered lists.
- For any destructive or write operation, show a summary of what will happen
  and wait for the user to confirm before proceeding.
- If a requested action involves sensitive data, remind the user of the
  privacy-first policy and offer a safe alternative.
"""

# ── Agent definition ──────────────────────────────────────────────────────────
root_agent = Agent(
    name="lifepilot_agent",
    model="gemini-2.0-flash",
    description=(
        "LifePilot — a privacy-first personal assistant that helps you plan "
        "your day, prioritize tasks, summarize notes, and draft reminders safely."
    ),
    instruction=SYSTEM_INSTRUCTION,
    tools=[
        # Task management
        list_tasks,
        add_task,
        update_task_status,

        # Calendar & free-time
        get_today_calendar,
        check_free_time,

        # Notes
        read_notes,
        summarize_notes_basic,

        # Reminders (draft-first, confirm-second)
        create_reminder_draft,
        confirm_reminder,
    ],
)
