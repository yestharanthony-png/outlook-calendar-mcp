from datetime import timedelta

from config.settings import DEFAULT_DURATION

from helpers.datetime_helper import (
    parse_datetime,
    format_datetime,
)
from helpers.logger import logger

from tools.get_schedule import get_schedule
from tools.list_events import list_events
from tools.create_event import create_event


def meeting_exists(user_email, subject, start_dt, end_dt):
    """
    Check whether an identical meeting already exists
    in the organizer's calendar.
    """

    events = list_events(user_email)

    for event in events.get("value", []):

        existing_subject = event.get("subject", "").strip().lower()

        existing_start = event["start"]["dateTime"].split(".")[0]

        existing_end = event["end"]["dateTime"].split(".")[0]

        if (
            existing_subject == subject.strip().lower()
            and existing_start == format_datetime(start_dt)
            and existing_end == format_datetime(end_dt)
        ):
            return True

    return False


def auto_schedule(
    user_emails,
    subject,
    search_start,
    search_end,
    duration_minutes=DEFAULT_DURATION
):
    """
    Automatically find the first common free slot
    and create a meeting.
    """

    result = get_schedule(
        user_emails=user_emails,
        start_time=search_start,
        end_time=search_end
    )

    duration = timedelta(minutes=duration_minutes)

    search_start_dt = parse_datetime(search_start)
    search_end_dt = parse_datetime(search_end)

    busy_slots = []

    # ------------------------------------
    # Collect busy slots of all users
    # ------------------------------------

    for user in result["value"]:

        for meeting in user["scheduleItems"]:

            busy_start = parse_datetime(
                meeting["start"]["dateTime"]
            )

            busy_end = parse_datetime(
                meeting["end"]["dateTime"]
            )

            busy_slots.append(
                (busy_start, busy_end)
            )

    # ------------------------------------
    # Sort busy slots
    # ------------------------------------

    busy_slots.sort(key=lambda slot: slot[0])

    # ------------------------------------
    # Merge overlapping busy slots
    # ------------------------------------

    merged = []

    for start, end in busy_slots:

        if not merged:

            merged.append([start, end])

        elif start <= merged[-1][1]:

            merged[-1][1] = max(
                merged[-1][1],
                end
            )

        else:

            merged.append([start, end])

    # ------------------------------------
    # Build attendee list
    # ------------------------------------

    attendees = []

    for email in user_emails[1:]:

        attendees.append(
            {
                "emailAddress": {
                    "address": email
                },
                "type": "required"
            }
        )

    current = search_start_dt

    # ------------------------------------
    # Search first common free slot
    # ------------------------------------

    for start, end in merged:

        if current + duration <= start:

            proposed_start = current
            proposed_end = current + duration

            if meeting_exists(
                user_emails[0],
                subject,
                proposed_start,
                proposed_end
            ):

                logger.warning("Meeting already exists.")

                return {
                    "message": "Meeting already exists.",
                    "subject": subject,
                    "start": proposed_start.isoformat(),
                    "end": proposed_end.isoformat()
                }

            logger.info("Common free slot found.")
            logger.info(
                f"{proposed_start} -> {proposed_end}"
            )

            return create_event(
                user_email=user_emails[0],
                subject=subject,
                start_time=format_datetime(proposed_start),
                end_time=format_datetime(proposed_end),
                attendees=attendees
            )

        if end > current:
            current = end

    # ------------------------------------
    # Schedule after last meeting
    # ------------------------------------

    if current + duration <= search_end_dt:

        proposed_start = current
        proposed_end = current + duration

        if meeting_exists(
            user_emails[0],
            subject,
            proposed_start,
            proposed_end
        ):

            logger.warning("Meeting already exists.")

            return {
                "message": "Meeting already exists.",
                "subject": subject,
                "start": proposed_start.isoformat(),
                "end": proposed_end.isoformat()
            }

        logger.info("Scheduling after last meeting.")
        logger.info(
            f"{proposed_start} -> {proposed_end}"
        )

        return create_event(
            user_email=user_emails[0],
            subject=subject,
            start_time=format_datetime(proposed_start),
            end_time=format_datetime(proposed_end),
            attendees=attendees
        )

    # ------------------------------------
    # No slot found
    # ------------------------------------

    logger.warning("No common free slot available.")

    return {
        "message": "No common free slot available."
    }