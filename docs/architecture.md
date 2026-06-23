# LifePilot AI Architecture

## 1. Overview

LifePilot AI is designed as a privacy-first personal assistant. The assistant helps users plan their day, prioritize tasks, summarize notes, and create reminder drafts safely.

The project uses a lightweight agent-oriented architecture. It separates user interface, agent logic, tools, skills, data, and evaluation.

## 2. Current Demo Architecture

The current version runs in local mock demo mode.

```text id="gls0bt"
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

## 3. Main Components

### 3.1 Streamlit Web UI

Location:

```text id="dpl8pg"
web/streamlit_app.py
```

Purpose:

* Provide a simple interface for demo.
* Allow the user to chat with LifePilot.
* Display today plan, tasks, notes, reminder drafts, and safety logs.
* Work without Gemini API.

### 3.2 ADK Agent

Location:

```text id="t1hyac"
app/agent.py
```

Purpose:

* Define the LifePilot agent.
* Register tools.
* Provide system instructions.
* Support future Gemini/ADK execution.

### 3.3 Local Tools

Location:

```text id="hx7ec9"
app/tools/
```

Tools:

* `task_tool.py`
* `calendar_tool.py`
* `notes_tool.py`
* `reminder_tool.py`

Purpose:

* Read and manage local demo data.
* Keep deterministic logic outside the LLM.
* Support evaluation without external APIs.

### 3.4 Local Data

Location:

```text id="xmzwnq"
app/data/
```

Files:

* `tasks.json`
* `calendar.json`
* `notes.json`

Purpose:

* Provide safe sample data.
* Avoid using real personal information.
* Make the demo reproducible.

### 3.5 Skills

Location:

```text id="il8u0c"
skills/
```

Skills:

* `daily-planning`
* `task-prioritization`
* `note-summarization`
* `safe-reminder`
* `privacy-guard`

Purpose:

* Store reusable agent workflows.
* Keep instructions modular.
* Reduce context overload.
* Make agent behavior easier to evaluate.

### 3.6 Evaluation

Location:

```text id="g3ug9q"
evals/
```

Purpose:

* Test local tools.
* Verify safe reminder behavior.
* Confirm that reminder drafts require confirmation.
* Demonstrate project reliability.

## 4. Safety Architecture

LifePilot uses a confirmation-first workflow.

```text id="yrwhzk"
Sensitive user request
  ↓
Create draft
  ↓
Show draft summary
  ↓
Ask user for confirmation
  ↓
Confirm only after user approval
```

This design prevents unsafe automatic actions.

## 5. Privacy Architecture

The current demo uses local sample data only.

Privacy rules:

1. Do not expose credentials.
2. Do not store secrets in logs.
3. Do not call external APIs in mock mode.
4. Do not use real Gmail or Calendar data.
5. Do not confirm reminders automatically.

## 6. Future Production Architecture

A future production version can use Google Cloud.

```text id="iie3gg"
User
  ↓
Web UI
  ↓
Cloud Run
  ↓
Pub/Sub
  ↓
Agent Runtime
  ↓
ADK Agent
  ↓
Skills + Tools
  ↓
Google Calendar / Gmail / Database
  ↓
Cloud Logging / Trace / Evaluation
```

## 7. Why This Architecture

This architecture was chosen because it is:

* Simple enough for local demo.
* Safe for personal data.
* Easy to test.
* Easy to explain in a project submission.
* Compatible with future ADK and Agent Runtime deployment.

## 8. Summary

LifePilot AI demonstrates how to design a useful personal assistant with safety and evaluation built in from the beginning. The mock UI allows the project to be demonstrated even when external model access is unavailable, while the ADK structure keeps the project ready for future production deployment.
    