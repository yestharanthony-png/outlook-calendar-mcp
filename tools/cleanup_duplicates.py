from services.calendar_service import CalendarService

calendar = CalendarService()


def cleanup_duplicates(user_email):
    return calendar.cleanup_duplicates(user_email)