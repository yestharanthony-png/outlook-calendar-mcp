from services.calendar_service import CalendarService


def update_event(
    user_email,
    event_id,
    subject,
    start_time,
    end_time,
):
    """
    Update an existing calendar event.
    """
    calendar = CalendarService()
    return calendar.update_event(
        user_email,
        event_id,
        subject,
        start_time,
        end_time,
    )