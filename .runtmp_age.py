import datetime

now = datetime.datetime.now(datetime.timezone.utc)
timestamps = [
    "2026-07-25T08:19:27Z",
    "2026-07-25T08:19:24Z",
    "2026-07-21T21:26:59Z",
    "2026-07-14T18:48:52Z",
    "2026-07-15T19:21:18Z",
    "2026-04-05T22:08:47Z",
    "2026-02-26T15:40:27Z",
    "2026-02-04T16:31:32Z",
    "2026-07-14T18:49:15Z",
    "2026-07-14T18:48:58Z",
    "2026-07-09T20:35:14Z",
]
print("NOW", now.isoformat())
for ts in timestamps:
    dt = datetime.datetime.strptime(ts, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=datetime.timezone.utc)
    hours = (now - dt).total_seconds() / 3600
    print(ts, "->", round(hours), "h")
