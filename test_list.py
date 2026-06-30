from tools.list_events import list_events

# Use an invalid email to test the error handler
USER_EMAIL = "User1@swp14.onmicrosoft.com"

# This line was missing
events = list_events(USER_EMAIL)

print("\nCalendar Events\n")

for event in events.get("value", []):

    print("-------------------------")
    print("Subject :", event.get("subject"))
    print("Start   :", event.get("start", {}).get("dateTime"))
    print("End     :", event.get("end", {}).get("dateTime"))
    print("ID      :", event.get("id"))

print("\nTotal Events:", len(events.get("value", [])))