from services.calendar_service import CalendarService

calendar = CalendarService()


def prepone_event(
    user_email,
    subject,
    minutes
):
    return calendar.reschedule_event(
        user_email=user_email,
        subject=subject,
        minutes=minutes,
        action="prepone"
    )