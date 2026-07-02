from services.calendar_service import CalendarService


def delete_event(
    user_email,
    event_id,
):
    """
    Delete a calendar event from Outlook.
    """
    calendar = CalendarService()

    return calendar.delete_event(
        user_email,
        event_id,
    )