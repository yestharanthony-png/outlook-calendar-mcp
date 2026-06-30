from services.calendar_service import CalendarService

calendar = CalendarService()


def delete_event(
    user_email,
    event_id,
):
    """
    Delete a calendar event from Outlook.
    """
    return calendar.delete_event(
        user_email,
        event_id,
    )