# docs/security_and_eval.md

# Security and Evaluation

## 1. Overview

LifePilot AI is designed with privacy and safety as core principles. Because personal assistants may handle sensitive tasks, notes, schedules, and reminders, the assistant must not act without clear user confirmation.

This document explains the project safety design and evaluation approach.

## 2. Safety Goals

The assistant should:

1. Help the user organize daily life.
2. Avoid exposing sensitive information.
3. Use local demo data by default.
4. Require confirmation before sensitive actions.
5. Avoid performing irreversible actions automatically.
6. Keep behavior transparent through a safety log.

## 3. Privacy-first Design

The current demo does not use real personal accounts.

It uses:

```text id="v9ojz6"
app/data/tasks.json
app/data/calendar.json
app/data/notes.json
```

This prevents accidental exposure of real user information.

## 4. Sensitive Data Handling

The assistant must not reveal or store:

```text id="3dkrje"
API keys
Passwords
Tokens
Private credentials
Sensitive personal information
```

If the user provides sensitive information, the assistant should avoid repeating it unnecessarily.

## 5. Confirmation-first Workflow

For reminder creation, the assistant follows this workflow:

```text id="vrktkn"
User asks for reminder
  ↓
Assistant creates draft
  ↓
Assistant marks draft as requiring confirmation
  ↓
User reviews the draft
  ↓
User confirms manually
```

The assistant must not confirm reminders automatically.

## 6. Evaluation Goals

The evaluation suite checks:

1. Task loading.
2. Calendar free-time checking.
3. Note summarization.
4. Reminder draft creation.
5. Reminder confirmation safety.
6. Basic privacy behavior.

## 7. Evaluation Files

```text id="s8nzp6"
evals/daily_planning_eval.json
evals/task_prioritization_eval.json
evals/note_summary_eval.json
evals/reminder_safety_eval.json
evals/privacy_eval.json
evals/run_evals.py
```

## 8. Running Evaluation

Run:

```bash id="qpt78n"
python evals/run_evals.py
```

Expected output:

```text id="z01277"
PASS: list_tasks returns a list
PASS: list_tasks has at least one task
PASS: check_free_time returns a dictionary
PASS: check_free_time includes suggested free blocks
PASS: read_notes returns a list
PASS: read_notes has at least one note
PASS: summarize_notes_basic returns a dictionary
PASS: summary includes action items
PASS: create_reminder_draft returns draft
PASS: reminder status is draft
PASS: reminder requires confirmation
```

## 9. Current Limitations

The current version:

1. Uses mock mode.
2. Does not call Gemini API.
3. Does not connect to real Google Calendar.
4. Does not send real reminders.
5. Uses local JSON files only.

These limitations are intentional for safe demonstration.

## 10. Future Safety Improvements

Future versions can add:

1. Real authentication.
2. Google Calendar permission control.
3. Gmail read-only mode.
4. Audit logs.
5. Role-based access.
6. Cloud Logging.
7. Agent Runtime monitoring.
8. Human confirmation for all write actions.

## 11. Conclusion

LifePilot AI demonstrates a safe personal assistant design. It is useful for planning and productivity, while still prioritizing privacy, confirmation, and evaluation.