from services.calendar_service import CalendarService


def postpone_event(
    user_email,
    subject,
    minutes,
):
    calendar = CalendarService()

    return calendar.reschedule_event(
        user_email=user_email,
        subject=subject,
        minutes=minutes,
        action="postpone",
    )