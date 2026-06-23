---
name: safe-reminder
description: |
  Draft safe reminders from user requests and ask for confirmation before saving or sending.
  Use when the user asks to remind them about a task, event, or deadline.
  Do NOT directly create, send, or delete reminders without explicit confirmation.
---

# Safe Reminder Skill

## Workflow
1. Extract reminder content.
2. Extract date and time.
3. Show a confirmation summary.
4. Ask the user to confirm.
5. Only after confirmation, call the reminder tool.