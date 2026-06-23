reminder_drafts = []


def create_reminder_draft(content: str, reminder_time: str):
    """
    Create a reminder draft.
    This does NOT save or send the reminder yet.
    User confirmation is required.
    """
    draft_id = len(reminder_drafts) + 1

    draft = {
        "id": draft_id,
        "content": content,
        "reminder_time": reminder_time,
        "status": "draft",
        "requires_confirmation": True
    }

    reminder_drafts.append(draft)

    return {
        "message": "Reminder draft created. Please confirm before saving.",
        "draft": draft
    }


def confirm_reminder(draft_id: int):
    """Confirm and activate a reminder draft."""
    for draft in reminder_drafts:
        if draft["id"] == draft_id:
            draft["status"] = "confirmed"
            draft["requires_confirmation"] = False

            return {
                "message": "Reminder confirmed successfully.",
                "reminder": draft
            }

    return {"error": "Reminder draft not found"}