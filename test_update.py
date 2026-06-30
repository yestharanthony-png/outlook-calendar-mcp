from tools.update_event import update_event

result = update_event(
    user_email="User1@swp14.onmicrosoft.com",
    event_id="AAMkADViNTA4ZTVlLTI5OTItNDRkOS1hODllLWY1YzQ1NjgzZjk4YgBGAAAAAAAX9a-xEJ1pQYEbu73tVpCdBwDq1Ra2-MssTrIHW4mIK3EFAAAAAAENAADq1Ra2-MssTrIHW4mIK3EFAAOeu0KTAAA=",
    subject="Testing Updated",
    start_time="2026-06-29T11:00:00",
    end_time="2026-06-29T12:00:00"
)

print(result)