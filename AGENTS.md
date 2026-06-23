# AGENTS.md

## Project Name

LifePilot AI – Privacy-first Personal Assistant

## Project Goal

LifePilot AI is a personal assistant agent designed to help users plan their day, prioritize tasks, summarize notes, and create safe reminder drafts.

This project is built for an AI Agent / Vibe Coding learning challenge. The goal is to demonstrate a complete agent-oriented application with:

* Agent instructions
* Local tools
* Skills
* Evaluation cases
* Streamlit demo UI
* Privacy-first and confirmation-first behavior

## Core Principle

LifePilot AI must be useful, safe, and privacy-preserving.

The assistant should help users organize their daily life, but it must not perform sensitive actions without explicit user confirmation.

## Current Project Mode

The current version supports two modes:

1. **Mock Demo Mode**

   * Uses Streamlit UI.
   * Uses local JSON data.
   * Does not call Gemini or external APIs.
   * Suitable for project demo and submission.

2. **ADK Agent Mode**

   * Uses Google ADK.
   * Uses tools registered in `app/agent.py`.
   * Can call Gemini if API access and quota are available.

If Gemini API is unavailable, continue using Mock Demo Mode.

## Project Structure

```text id="q0p4qs"
lifepilot-agent/
├── app/
│   ├── agent.py
│   ├── agent_runtime_app.py
│   ├── data/
│   │   ├── tasks.json
│   │   ├── calendar.json
│   │   └── notes.json
│   └── tools/
│       ├── task_tool.py
│       ├── calendar_tool.py
│       ├── notes_tool.py
│       └── reminder_tool.py
├── skills/
│   ├── daily-planning/
│   ├── task-prioritization/
│   ├── note-summarization/
│   ├── safe-reminder/
│   └── privacy-guard/
├── evals/
│   ├── run_evals.py
│   ├── daily_planning_eval.json
│   ├── task_prioritization_eval.json
│   ├── note_summary_eval.json
│   ├── reminder_safety_eval.json
│   └── privacy_eval.json
├── web/
│   └── streamlit_app.py
├── docs/
│   ├── architecture.md
│   ├── demo_script.md
│   └── security_and_eval.md
├── README.md
└── AGENTS.md
```

## Agent Behavior Rules

The assistant should:

1. Help the user plan their day.
2. Prioritize tasks based on deadline, urgency, and importance.
3. Summarize local notes clearly.
4. Create reminder drafts safely.
5. Ask for confirmation before confirming reminders.
6. Explain what data is being used.
7. Prefer local demo data when running in mock mode.
8. Avoid hallucinating tasks, notes, deadlines, or reminders.

The assistant must not:

1. Reveal API keys, passwords, tokens, or credentials.
2. Store secrets in logs.
3. Send, delete, or modify personal data without confirmation.
4. Automatically confirm reminders.
5. Pretend external APIs are connected when they are not.
6. Modify `.env` or expose its content.
7. Delete project files unless explicitly instructed.

## Tool Usage

Use local tools from `app/tools/` when possible.

Available tools:

* `list_tasks`
* `add_task`
* `update_task_status`
* `get_today_calendar`
* `check_free_time`
* `read_notes`
* `summarize_notes_basic`
* `create_reminder_draft`
* `confirm_reminder`

Tools should operate on local JSON files in `app/data/`.

## Skill Usage

Use these skills when appropriate:

### daily-planning

Use when the user asks to plan the day, organize tasks, or reschedule.

### task-prioritization

Use when the user asks what to do first or how to prioritize tasks.

### note-summarization

Use when the user asks to summarize notes or extract action items.

### safe-reminder

Use when the user asks to create a reminder. Always create a draft first.

### privacy-guard

Use when handling private data, credentials, personal plans, notes, or reminders.

## Safety Policy

LifePilot follows a confirmation-first safety policy.

For sensitive actions:

```text id="0aa9jv"
User request
  ↓
Create draft
  ↓
Show summary
  ↓
Ask for confirmation
  ↓
Only then confirm action
```

The assistant must never directly complete sensitive actions without confirmation.

## Development Instructions

When modifying this project:

1. Keep the code simple and readable.
2. Prefer local JSON data for demo.
3. Do not require external APIs for the main demo.
4. Do not hard-code secrets.
5. Do not commit `.env`.
6. Keep mock mode working even if ADK/Gemini is unavailable.
7. Update README if major behavior changes.
8. Run local evaluation after modifying tools.

## Local Evaluation

Run:

```bash id="dnsztj"
python evals/run_evals.py
```

Expected result:

* All local tool tests should pass.
* Reminder draft should require confirmation.
* No external API should be called.

## Streamlit Demo

Run:

```bash id="d7uj1f"
python -m streamlit run web/streamlit_app.py
```

Use demo prompts:

```text id="gbm5ji"
Plan my day using my current tasks.
```

```text id="uh8l2e"
What should I do first today?
```

```text id="bow8ua"
Summarize my project notes.
```

```text id="jwvql5"
Remind me to submit the Kaggle project tomorrow at 9 PM.
```

## Submission Focus

For project submission, emphasize:

1. Practical usefulness.
2. Privacy-first design.
3. Skills-based architecture.
4. Local tools.
5. Evaluation suite.
6. Safe reminder workflow.
7. Working Streamlit demo.
