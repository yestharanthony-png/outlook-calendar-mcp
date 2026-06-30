from tools.prepone_event import prepone_event

result = prepone_event(
    user_email="User1@swp14.onmicrosoft.com",
    event_id="<EVENT_ID>",
    minutes=30
)

print(result)