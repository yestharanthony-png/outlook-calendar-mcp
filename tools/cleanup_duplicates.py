from services.calendar_service import CalendarService


def cleanup_duplicates(user_email):
    calendar = CalendarService()
    return calendar.cleanup_duplicates(user_email)