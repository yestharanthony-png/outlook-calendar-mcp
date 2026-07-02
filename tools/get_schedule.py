from services.calendar_service import CalendarService


def get_schedule(
    user_emails,
    start_time,
    end_time,
):
    """
    Retrieve calendar availability for multiple users.
    """
    calendar = CalendarService()
    return calendar.get_schedule(
        user_emails,
        start_time,
        end_time,
    )