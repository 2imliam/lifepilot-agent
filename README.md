# LifePilot AI – Privacy-first Personal Assistant

## 1. Project Overview

**LifePilot AI** is a privacy-first personal assistant designed to help users organize their daily life. The assistant can plan a user's day, prioritize tasks, summarize personal notes, and create safe reminder drafts.

This project was built as part of an AI Agent / Vibe Coding learning track. It demonstrates how an AI assistant can be designed using an agent-oriented architecture with tools, skills, evaluation cases, and a user interface.

The current version includes a **mock demo mode** that does not call external APIs. This allows the project to be tested and demonstrated locally even without an active Gemini API quota.

---

## 2. Problem Statement

People often manage their daily tasks, deadlines, reminders, and notes across many different apps. This creates several problems:

* Important tasks are forgotten.
* Deadlines are missed.
* Notes are hard to summarize quickly.
* Users feel overwhelmed when many tasks compete for attention.
* Personal data can be exposed if an assistant acts without clear safety controls.

LifePilot AI addresses these problems by giving users a simple assistant that helps them organize tasks and reminders while following a privacy-first and confirmation-first design.

---

## 3. Solution

LifePilot AI helps users:

1. Create a structured daily plan from current tasks.
2. Prioritize tasks based on urgency and importance.
3. Summarize personal project notes.
4. Create reminder drafts safely.
5. Require confirmation before performing sensitive actions.
6. Use local sample data for safe demonstration.

Unlike a simple chatbot, LifePilot AI is designed around an agent architecture:

* **Skills** define reusable workflows.
* **Tools** perform deterministic actions on local data.
* **Evaluations** verify core behaviors.
* **UI** provides a clear demo interface.
* **Safety rules** prevent automatic sensitive actions.

---

## 4. Key Features

### 4.1 Daily Planning

The assistant can read current tasks and generate a structured plan for the day.

Example prompt:

```text
Plan my day using my current tasks.
```

Expected behavior:

* Read task data.
* Check task priority.
* Arrange tasks into time blocks.
* Keep the plan realistic.
* Avoid creating reminders automatically.

---

### 4.2 Task Prioritization

The assistant can identify what the user should do first.

Example prompt:

```text
What should I do first today?
```

Expected behavior:

* Rank tasks by priority.
* Consider deadlines.
* Explain why each task is important.

---

### 4.3 Notes Summarization

The assistant can summarize local project notes and extract action items.

Example prompt:

```text
Summarize my project notes.
```

Expected behavior:

* Read local notes.
* Summarize key points.
* Extract useful action items.

---

### 4.4 Safe Reminder Drafting

The assistant can create a reminder draft but does not confirm it automatically.

Example prompt:

```text
Remind me to submit the Kaggle project tomorrow at 9 PM.
```

Expected behavior:

* Create a reminder draft.
* Mark it as requiring confirmation.
* Ask the user before confirming the reminder.
* Never send, save, or modify real data automatically.

---

### 4.5 Privacy and Safety Log

The UI includes a safety log that explains important safety behavior:

* Mock mode is enabled.
* No Gemini API calls are made.
* Local JSON data is used.
* Write actions require confirmation.

---

## 5. Architecture

The project follows a simple agent-oriented architecture.

```text
User
  ↓
Streamlit Web UI
  ↓
Mock Agent Logic
  ↓
Local Tools
  ↓
Local JSON Data
  ↓
Evaluation Suite
```

Target production architecture:

```text
User
  ↓
Web UI
  ↓
Cloud Run
  ↓
Pub/Sub
  ↓
ADK Agent Runtime
  ↓
ADK Agent
  ↓
Skills + Tools
  ↓
User Data Sources
```

---

## 6. Technology Stack

| Component            | Technology                      |
| -------------------- | ------------------------------- |
| Agent Framework      | Google ADK                      |
| Programming Language | Python                          |
| UI                   | Streamlit                       |
| Data Storage         | Local JSON files                |
| Evaluation           | Local Python evaluation script  |
| Skills               | SKILL.md-based workflow folders |
| Demo Mode            | Mock local execution            |
| Future Deployment    | Agent Runtime / Cloud Run       |

---

## 7. Project Structure

```text
lifepilot-agent/
├── README.md
├── AGENTS.md
├── app/
│   ├── agent.py
│   ├── tools/
│   │   ├── task_tool.py
│   │   ├── calendar_tool.py
│   │   ├── notes_tool.py
│   │   └── reminder_tool.py
│   └── data/
│       ├── tasks.json
│       ├── calendar.json
│       └── notes.json
├── skills/
│   ├── daily-planning/
│   │   └── SKILL.md
│   ├── task-prioritization/
│   │   └── SKILL.md
│   ├── note-summarization/
│   │   └── SKILL.md
│   ├── safe-reminder/
│   │   └── SKILL.md
│   └── privacy-guard/
│       └── SKILL.md
├── evals/
│   ├── daily_planning_eval.json
│   ├── task_prioritization_eval.json
│   ├── note_summary_eval.json
│   ├── reminder_safety_eval.json
│   ├── privacy_eval.json
│   └── run_evals.py
├── web/
│   └── streamlit_app.py
└── docs/
    ├── architecture.md
    ├── demo_script.md
    └── security_and_eval.md
```

---

## 8. Agent Skills

The project includes five core skills.

### 8.1 daily-planning

Purpose:

* Create a realistic daily schedule from tasks, deadlines, and available time.

Used when:

* The user asks to plan the day.
* The user asks to organize tasks.
* The user asks to reschedule tasks.

---

### 8.2 task-prioritization

Purpose:

* Prioritize tasks based on urgency, importance, and deadline.

Used when:

* The user asks what to do first.
* The user feels overwhelmed.
* The user needs a task ranking.

---

### 8.3 note-summarization

Purpose:

* Summarize notes and extract action items.

Used when:

* The user asks to summarize personal notes.
* The user wants key points from project notes.
* The user wants a checklist from long text.

---

### 8.4 safe-reminder

Purpose:

* Create safe reminder drafts that require confirmation.

Used when:

* The user asks to be reminded about something.
* The assistant needs to prepare a reminder safely.

Safety rule:

* The assistant must not confirm or send reminders automatically.

---

### 8.5 privacy-guard

Purpose:

* Protect sensitive personal data.

Used when:

* The assistant handles private notes, tasks, reminders, credentials, or personal plans.

Safety rule:

* Never expose secrets such as API keys, passwords, or tokens.

---

## 9. Local Tools

The assistant uses local Python tools.

### task_tool.py

Functions:

```text
list_tasks()
add_task(title, deadline, priority)
update_task_status(task_id, status)
```

### calendar_tool.py

Functions:

```text
get_today_calendar()
check_free_time()
```

### notes_tool.py

Functions:

```text
read_notes()
summarize_notes_basic(note_id)
```

### reminder_tool.py

Functions:

```text
create_reminder_draft(content, reminder_time)
confirm_reminder(draft_id)
```

---

## 10. How to Run the Project

### 10.1 Install dependencies

```bash
python -m pip install streamlit
```

Optional:

```bash
python -m pip install google-adk
```

---

### 10.2 Run local evaluation

```bash
python evals/run_evals.py
```

Expected output:

```text
Running LifePilot local evaluation suite...

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

Evaluation completed.
```

---

### 10.3 Run the Streamlit UI

```bash
python -m streamlit run web/streamlit_app.py
```

Open the local URL shown in the terminal, usually:

```text
http://localhost:8501
```

---

### 10.4 Optional: Run ADK Agent

If Gemini API access is available:

```bash
adk run app
```

Example prompt:

```text
Plan my day using my current tasks.
```

If Gemini quota or API access is unavailable, use the Streamlit mock UI for demonstration.

---

## 11. Demo Prompts

Use these prompts in the UI demo.

### Prompt 1: Daily Planning

```text
Plan my day using my current tasks.
```

Expected result:

* A structured plan using current tasks.

---

### Prompt 2: Priority

```text
What should I do first today?
```

Expected result:

* A ranked list of tasks.

---

### Prompt 3: Notes Summary

```text
Summarize my project notes.
```

Expected result:

* Short summary and action items.

---

### Prompt 4: Safe Reminder

```text
Remind me to submit the Kaggle project tomorrow at 9 PM.
```

Expected result:

* A reminder draft is created.
* The assistant asks for confirmation.
* The reminder is not confirmed automatically.

---

## 12. Evaluation Design

The project includes local evaluation cases for:

| Evaluation File               | Purpose                            |
| ----------------------------- | ---------------------------------- |
| daily_planning_eval.json      | Checks daily planning behavior     |
| task_prioritization_eval.json | Checks task ranking behavior       |
| note_summary_eval.json        | Checks note summarization          |
| reminder_safety_eval.json     | Checks safe reminder drafting      |
| privacy_eval.json             | Checks privacy protection behavior |
| run_evals.py                  | Runs local evaluation tests        |

The evaluation suite focuses on:

1. Functional behavior.
2. Safety behavior.
3. Local tool correctness.
4. Confirmation-first reminder design.
5. Privacy-first assistant behavior.

---

## 13. Safety and Privacy Design

LifePilot AI follows a privacy-first design.

### Safety Rules

1. The assistant uses local sample data by default.
2. The assistant does not call external APIs in mock demo mode.
3. The assistant never confirms reminders automatically.
4. The assistant never sends, deletes, or modifies personal data without explicit user confirmation.
5. The assistant avoids exposing secrets such as API keys, passwords, or tokens.
6. The assistant uses a visible safety log to show important safety actions.

### Confirmation-first Design

For sensitive actions, the assistant follows this flow:

```text
User request
  ↓
Assistant creates draft
  ↓
Assistant asks for confirmation
  ↓
User confirms
  ↓
Action is marked confirmed
```

This prevents accidental or unsafe actions.

---

## 14. Current Limitations

The current version is a local demo and has several limitations:

1. Gemini API may not be available depending on quota or project access.
2. The Streamlit UI uses mock local logic instead of calling a live LLM.
3. The assistant uses local JSON files instead of real Google Calendar or Gmail.
4. Reminder actions are simulated and not connected to a real notification system.
5. The UI is designed for demonstration, not production deployment.

---

## 15. Future Improvements

Future versions can include:

1. Gemini API integration when quota is available.
2. Google Calendar integration.
3. Gmail or email summary integration.
4. Real reminder notifications.
5. Cloud Run deployment.
6. Agent Runtime deployment.
7. Pub/Sub event-based workflow.
8. User authentication.
9. Persistent database storage.
10. Mobile-friendly UI.

---

## 16. Demo Video Script

Suggested demo flow:

1. Introduce the problem.
2. Show the LifePilot AI dashboard.
3. Ask the assistant to plan the day.
4. Ask the assistant to prioritize tasks.
5. Ask the assistant to summarize notes.
6. Ask the assistant to create a reminder.
7. Show that the reminder is only a draft.
8. Show the safety log.
9. Explain the evaluation suite.
10. Conclude with future improvements.

---

## 17. Why This Project Matters

LifePilot AI demonstrates a practical and safe direction for personal AI assistants.

The project is useful because it helps users manage daily planning and personal productivity.

The project is safe because it uses:

* Local sample data.
* Confirmation-first actions.
* Privacy protection rules.
* Evaluation cases.
* Mock demo mode when external APIs are unavailable.

---

## 18. Author

**Project:** LifePilot AI – Privacy-first Personal Assistant
**Category:** Personal Assistant
**Built with:** Python, Google ADK, Streamlit, Agent Skills, Local Tools, Evaluation Suite

---

## 19. License

This project is for educational and demonstration purposes.
