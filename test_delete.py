from tools.list_events import list_events
from tools.delete_event import delete_event

USER_EMAIL = "User1@swp14.onmicrosoft.com"
SUBJECT = "Testing Updated"

# Get all events
events = list_events(USER_EMAIL)

event_found = False

for event in events.get("value", []):

    if event["subject"].strip().lower() == SUBJECT.lower():

        event_found = True

        print("Deleting event...")
        print("----------------------------")
        print("Subject :", event["subject"])
        print("Start   :", event["start"]["dateTime"])
        print("ID      :", event["id"])

        result = delete_event(
            user_email=USER_EMAIL,
            event_id=event["id"]
        )

        print("\nDelete Result:")
        print(result)

        break

if not event_found:
    print(f"No event found with subject '{SUBJECT}'.")