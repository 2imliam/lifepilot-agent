---
name: privacy-guard
description: |
  Detect sensitive personal data and enforce privacy-safe behavior.
  Use when the agent handles emails, notes, reminders, credentials, private plans, or personal information.
  Do NOT expose, log, or repeat secrets unnecessarily.
---

# Privacy Guard Skill

## Rules
1. Never reveal API keys, passwords, tokens, or private credentials.
2. Do not send messages, delete data, or modify schedules without confirmation.
3. Prefer local/sample data for demos.
4. Explain what data is being used.
5. If the request is risky, ask for confirmation.