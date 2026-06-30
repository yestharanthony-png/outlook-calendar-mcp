from services.calendar_service import CalendarService

calendar = CalendarService()


def postpone_event(
    user_email,
    event_id,
    minutes
):

    return calendar.reschedule_event(
        user_email=user_email,
        event_id=event_id,
        minutes=minutes,
        action="postpone"
    )