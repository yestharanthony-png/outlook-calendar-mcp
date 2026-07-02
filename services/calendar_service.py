from datetime import datetime, timedelta

from config.settings import (
    GRAPH_BASE_URL,
    TIMEZONE,
    AVAILABILITY_INTERVAL
)

from services.graph_service import GraphService


class CalendarService:
    """
    Calendar business logic.
    """

    def __init__(self):

        self.graph = GraphService()

    # ----------------------------------
    # List Events
    # ----------------------------------

    def list_events(
        self,
        user_email: str
    ):

        url = (
    f"{GRAPH_BASE_URL}"
    f"/users/{user_email}/calendar/events"
    f"?$orderby=createdDateTime desc"
)

        return self.graph.get(url)

    # ----------------------------------
    # Create Event
    # ----------------------------------

    def create_event(
        self,
        user_email,
        subject,
        start_time,
        end_time,
        attendees=None
    ):

        url = (
            f"{GRAPH_BASE_URL}"
            f"/users/{user_email}/events"
        )

        body = {
            "subject": subject,
            "start": {
                "dateTime": start_time,
                "timeZone": TIMEZONE
            },
            "end": {
                "dateTime": end_time,
                "timeZone": TIMEZONE
            },
            "attendees": attendees or []
        }

        return self.graph.post(
            url,
            body
        )

    # ----------------------------------
    # Update Event
    # ----------------------------------

    def update_event(
        self,
        user_email,
        event_id,
        subject,
        start_time,
        end_time
    ):

        url = (
            f"{GRAPH_BASE_URL}"
            f"/users/{user_email}/events/{event_id}"
        )

        body = {
            "subject": subject,
            "start": {
                "dateTime": start_time,
                "timeZone": TIMEZONE
            },
            "end": {
                "dateTime": end_time,
                "timeZone": TIMEZONE
            }
        }

        return self.graph.patch(
            url,
            body
        )

    # ----------------------------------
    # Delete Event
    # ----------------------------------

    def delete_event(
        self,
        user_email,
        event_id
    ):

        url = (
            f"{GRAPH_BASE_URL}"
            f"/users/{user_email}/events/{event_id}"
        )

        return self.graph.delete(url)

    # ----------------------------------
    # Get Schedule
    # ----------------------------------

    def get_schedule(
        self,
        user_emails,
        start_time,
        end_time
    ):

        url = (
            f"{GRAPH_BASE_URL}"
            f"/users/{user_emails[0]}"
            f"/calendar/getSchedule"
        )

        body = {
            "schedules": user_emails,
            "startTime": {
                "dateTime": start_time,
                "timeZone": TIMEZONE
            },
            "endTime": {
                "dateTime": end_time,
                "timeZone": TIMEZONE
            },
            "availabilityViewInterval": AVAILABILITY_INTERVAL
        }

        return self.graph.post(
            url,
            body
        )
    # ----------------------------------
    # Reschedule Event
    # ----------------------------------

    def reschedule_event(
        self,
        user_email,
        subject,
        minutes,
        action,
    ):
        """
        Prepone or postpone the latest meeting matching the subject.
        """

        events = self.list_events(user_email)

        matching_events = [
            event
            for event in events.get("value", [])
            if event["subject"].strip().lower() == subject.strip().lower()
        ]

        if not matching_events:
            return {
                "message": "Meeting not found."
            }

        # Pick the newest meeting if duplicates exist
        matching_events.sort(
            key=lambda x: x["createdDateTime"],
            reverse=True,
        )

        event = matching_events[0]

        start_dt = datetime.fromisoformat(
            event["start"]["dateTime"].split(".")[0]
        )

        end_dt = datetime.fromisoformat(
            event["end"]["dateTime"].split(".")[0]
        )

        delta = timedelta(minutes=minutes)

        if action == "postpone":
            new_start = start_dt + delta
            new_end = end_dt + delta

        elif action == "prepone":
            new_start = start_dt - delta
            new_end = end_dt - delta

        else:
            return {
                "message": "Invalid action."
            }

        return self.update_event(
            user_email=user_email,
            event_id=event["id"],
            subject=event["subject"],
            start_time=new_start.strftime("%Y-%m-%dT%H:%M:%S"),
            end_time=new_end.strftime("%Y-%m-%dT%H:%M:%S"),
        )
    # ----------------------------------
    # Cleanup Duplicate Meetings
    # ----------------------------------

    def cleanup_duplicates(self, user_email):
        """
        Remove duplicate meetings while keeping the newest one.
        """

        events = self.list_events(user_email)

        grouped = {}

        for event in events.get("value", []):

            organizer = (
                event.get("organizer", {})
                     .get("emailAddress", {})
                     .get("address", "")
                     .lower()
            )

            attendees = tuple(
                sorted(
                    attendee["emailAddress"]["address"].lower()
                    for attendee in event.get("attendees", [])
                )
            )

            key = (
                event["subject"].strip().lower(),
                event["start"]["dateTime"],
                event["end"]["dateTime"],
                organizer,
                attendees,
            )

            grouped.setdefault(key, []).append(event)

        deleted = []

        for meetings in grouped.values():

            if len(meetings) <= 1:
                continue

            meetings.sort(
                key=lambda x: x["createdDateTime"],
                reverse=True,
            )

            for duplicate in meetings[1:]:

                self.delete_event(
                    user_email,
                    duplicate["id"],
                )

                deleted.append(duplicate["id"])

        return {
            "duplicates_removed": len(deleted),
            "deleted_ids": deleted,
        }
        