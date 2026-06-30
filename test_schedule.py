from tools.get_schedule import get_schedule

result = get_schedule(
    user_emails=[
        "User1@swp14.onmicrosoft.com",
        "igenticuser1@swp14.onmicrosoft.com"
    ],
    start_time="2026-06-29T09:00:00",
    end_time="2026-06-29T17:00:00"
)

print(result)