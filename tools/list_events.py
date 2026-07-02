from services.calendar_service import CalendarService

def list_events(user_email):
    """
    Retrieve all calendar events for the specified Outlook user.
    """
    calendar = CalendarService()   # Create a fresh instance every call
    return calendar.list_events(user_email)