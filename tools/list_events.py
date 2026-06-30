from services.calendar_service import CalendarService

calendar = CalendarService()


def list_events(user_email):
    """
    Retrieve all calendar events for the specified Outlook user.
    """
    return calendar.list_events(user_email)