# docs/demo_script.md

# LifePilot AI Demo Script

## 1. Demo Goal

This demo shows how LifePilot AI helps users plan their day, prioritize tasks, summarize notes, and create safe reminder drafts.

The demo runs in local mock mode, so it does not require Gemini API access.

## 2. Demo Duration

Recommended video length:

```text id="p1p246"
3 to 5 minutes
```

## 3. Opening

Say:

```text id="nml8iy"
Hello, this is LifePilot AI, a privacy-first personal assistant. It helps users organize daily tasks, prioritize work, summarize notes, and create safe reminder drafts. The project is designed with safety, privacy, tools, skills, and evaluation in mind.
```

## 4. Show Project Structure

Show the folders:

```text id="45249r"
app/
skills/
evals/
web/
docs/
README.md
AGENTS.md
```

Say:

```text id="40ajrq"
The project is organized into tools, skills, evaluations, documentation, and a Streamlit demo interface.
```

## 5. Show Streamlit UI

Run:

```bash id="3c1cq3"
python -m streamlit run web/streamlit_app.py
```

Open the local URL.

Say:

```text id="b1or98"
This is the LifePilot dashboard. It includes a chat panel, today plan, task table, notes summary, reminder drafts, and safety log.
```

## 6. Demo Daily Planning

Type:

```text id="k0lgc0"
Plan my day using my current tasks.
```

Say:

```text id="s52wb5"
The assistant reads local task data and creates a structured plan for the day.
```

## 7. Demo Task Prioritization

Type:

```text id="ch4vqj"
What should I do first today?
```

Say:

```text id="byw78t"
The assistant ranks tasks based on priority and deadline.
```

## 8. Demo Notes Summary

Type:

```text id="un9f4o"
Summarize my project notes.
```

Say:

```text id="ufp19k"
The assistant summarizes local project notes and extracts action items.
```

## 9. Demo Safe Reminder

Type:

```text id="ftxj35"
Remind me to submit the Kaggle project tomorrow at 9 PM.
```

Say:

```text id="h3ff3c"
The assistant creates a reminder draft, but it does not confirm or send the reminder automatically.
```

Show the Reminder Drafts tab.

Say:

```text id="6eplf8"
This demonstrates the confirmation-first safety design.
```

## 10. Show Safety Log

Open the Safety Log tab.

Say:

```text id="nom2nz"
The safety log shows that mock mode is enabled, local data is used, and write actions require confirmation.
```

## 11. Show Evaluation

Run:

```bash id="w9bpj0"
python evals/run_evals.py
```

Say:

```text id="c7sn9j"
The project includes local evaluation tests for task loading, calendar checking, note summarization, reminder drafting, and confirmation safety.
```

## 12. Closing

Say:

```text id="rmbra2"
LifePilot AI demonstrates how a personal assistant can be useful while still being privacy-first and safety-aware. Future versions can connect to Gemini, Google Calendar, Gmail, and Agent Runtime when production API access is available.
```

---


