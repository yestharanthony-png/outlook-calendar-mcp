from services.calendar_service import CalendarService


def prepone_event(
    user_email,
    subject,
    minutes,
):
    calendar = CalendarService()

    return calendar.reschedule_event(
        user_email=user_email,
        subject=subject,
        minutes=minutes,
        action="prepone",
    )