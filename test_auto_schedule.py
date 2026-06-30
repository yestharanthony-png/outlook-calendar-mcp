from tools.auto_schedule import auto_schedule

result = auto_schedule(
    user_emails=[
        "User1@swp14.onmicrosoft.com",
        "igenticuser1@swp14.onmicrosoft.com"
    ],
    subject="Architecture Planning Meeting",
    search_start="2026-07-01T09:00:00",
    search_end="2026-07-01T17:00:00",
    duration_minutes=60
)

print("\nResult:\n")
print(result)