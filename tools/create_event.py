from services.calendar_service import CalendarService

calendar = CalendarService()


def create_event(
    user_email,
    subject,
    start_time,
    end_time,
    attendees=None,
):
    return calendar.create_event(
        user_email,
        subject,
        start_time,
        end_time,
        attendees,
    )