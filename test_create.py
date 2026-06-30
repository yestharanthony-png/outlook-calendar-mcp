from tools.create_event import create_event

result = create_event(
    user_email="User1@swp14.onmicrosoft.com",
    subject="Testing Refactor",
    start_time="2026-06-29T10:00:00",
    end_time="2026-06-29T11:00:00"
)

print(result)