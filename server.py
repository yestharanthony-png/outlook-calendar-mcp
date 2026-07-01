from fastmcp import FastMCP

from tools.list_events import list_events
from tools.create_event import create_event
from tools.update_event import update_event
from tools.delete_event import delete_event
from tools.get_schedule import get_schedule
from tools.auto_schedule import auto_schedule
from tools.prepone_event import prepone_event
from tools.postpone_event import postpone_event
from tools.cleanup_duplicates import cleanup_duplicates

mcp = FastMCP("Outlook Calendar MCP")


# ----------------------------------------------------
# List Calendar Events
# ----------------------------------------------------

@mcp.tool()
def list_calendar_events(user_email: str):
    """
    List all Outlook calendar events.
    """
    return list_events(user_email)


# ----------------------------------------------------
# Create Calendar Event
# ----------------------------------------------------

@mcp.tool()
def create_calendar_event(
    organizer: str,
    subject: str,
    start_time: str,
    end_time: str,
    attendees: list[str] = [],
):
    """
    Create a meeting with attendees.
    """

    attendee_list = [
        {
            "emailAddress": {
                "address": email
            },
            "type": "required"
        }
        for email in attendees
    ]

    return create_event(
        user_email=organizer,
        subject=subject,
        start_time=start_time,
        end_time=end_time,
        attendees=attendee_list,
    )


# ----------------------------------------------------
# Update Calendar Event
# ----------------------------------------------------

@mcp.tool()
def update_calendar_event(
    user_email: str,
    event_id: str,
    subject: str,
    start_time: str,
    end_time: str,
):
    """
    Update an existing Outlook calendar meeting.
    """
    return update_event(
        user_email=user_email,
        event_id=event_id,
        subject=subject,
        start_time=start_time,
        end_time=end_time,
    )


# ----------------------------------------------------
# Delete Calendar Event
# ----------------------------------------------------

@mcp.tool()
def delete_calendar_event(
    user_email: str,
    event_id: str,
):
    """
    Delete an Outlook calendar meeting.
    """
    return delete_event(
        user_email=user_email,
        event_id=event_id,
    )


# ----------------------------------------------------
# Get Calendar Schedule
# ----------------------------------------------------

@mcp.tool()
def get_calendar_schedule(
    user_emails: list[str],
    start_time: str,
    end_time: str,
):
    """
    Get free/busy schedule for multiple users.
    """
    return get_schedule(
        user_emails=user_emails,
        start_time=start_time,
        end_time=end_time,
    )


# ----------------------------------------------------
# Auto Schedule Meeting
# ----------------------------------------------------

@mcp.tool()
def auto_schedule_meeting(
    organizer: str,
    attendees: list[str],
    subject: str,
    search_start: str,
    search_end: str,
    duration_minutes: int = 60,
):
    """
    Automatically find a common free slot and create the meeting.
    """

    users = [organizer] + attendees

    return auto_schedule(
        user_emails=users,
        subject=subject,
        search_start=search_start,
        search_end=search_end,
        duration_minutes=duration_minutes,
    )


# ----------------------------------------------------
# Postpone Meeting
# ----------------------------------------------------

@mcp.tool()
def postpone_calendar_event(
    user_email: str,
    subject: str,
    minutes: int,
):
    """
    Postpone an existing meeting.
    """
    return postpone_event(
        user_email=user_email,
        subject=subject,
        minutes=minutes,
    )


# ----------------------------------------------------
# Prepone Meeting
# ----------------------------------------------------

@mcp.tool()
def prepone_calendar_event(
    user_email: str,
    subject: str,
    minutes: int,
):
    """
   Prepone an existing meeting.
    """
    return prepone_event(
        user_email=user_email,
        subject=subject,
        minutes=minutes,
    )


# ----------------------------------------------------
# Cleanup Duplicate Meetings
# ----------------------------------------------------

@mcp.tool()
def cleanup_duplicate_meetings(
    user_email: str,
):
    """
   Remove duplicate meetings while keeping the newest one.
    """
    return cleanup_duplicates(user_email)


# ----------------------------------------------------
# FastMCP HTTP App
# ----------------------------------------------------

app = mcp.http_app()


# ----------------------------------------------------
# Run Server
# ----------------------------------------------------

if __name__ == "__main__":
    mcp.run(
        transport="streamable-http",
        host="0.0.0.0",
        port=8000,
    )