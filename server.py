from fastmcp import FastMCP

from tools.list_events import list_events
from tools.create_event import create_event
from tools.update_event import update_event
from tools.delete_event import delete_event
from tools.get_schedule import get_schedule

mcp = FastMCP("Outlook Calendar MCP")


@mcp.tool()
def list_calendar_events(user_email: str):
    return list_events(user_email)


@mcp.tool()
def create_calendar_event(
    user_email: str,
    subject: str,
    start_time: str,
    end_time: str
):
    return create_event(
        user_email,
        subject,
        start_time,
        end_time
    )


@mcp.tool()
def update_calendar_event(
    user_email: str,
    event_id: str,
    subject: str
):
    return update_event(
        user_email,
        event_id,
        subject
    )


@mcp.tool()
def delete_calendar_event(
    user_email: str,
    event_id: str
):
    return delete_event(
        user_email,
        event_id
    )


@mcp.tool()
def get_calendar_schedule(
    user_email: str,
    start_time: str,
    end_time: str
):
    return get_schedule(
        user_email,
        start_time,
        end_time
    )


if __name__ == "__main__":
    mcp.run(
        transport="streamable-http",
        host="0.0.0.0",
        port=8000
    )