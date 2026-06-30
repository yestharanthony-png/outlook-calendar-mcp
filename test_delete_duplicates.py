from tools.list_events import list_events
from tools.delete_event import delete_event

USER_EMAIL = "User1@swp14.onmicrosoft.com"
SUBJECT = "Multi User Architecture Meeting"

events = list_events(USER_EMAIL)

duplicates = []

for event in events["value"]:
    if event["subject"] == SUBJECT:
        duplicates.append(event)

print(f"Found {len(duplicates)} meetings.")

# Keep the newest meeting and delete the rest
duplicates.sort(
    key=lambda x: x["createdDateTime"],
    reverse=True
)

for event in duplicates[1:]:

    print("--------------------------------")
    print("Deleting:", event["subject"])
    print("ID:", event["id"])

    result = delete_event(
        user_email=USER_EMAIL,
        event_id=event["id"]
    )

    print(result)

print("--------------------------------")
print("Duplicate cleanup completed.")