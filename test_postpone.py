from tools.postpone_event import postpone_event

result = postpone_event(
    user_email="User1@swp14.onmicrosoft.com",
    event_id="<EVENT_ID>",
    minutes=30
)

print(result)