from datetime import datetime, timezone
now = datetime(2026,7,24,10,38,42, tzinfo=timezone.utc)
times = {
 "applications#26": "2026-07-21T21:26:59Z",
 "applications#18": "2026-07-15T19:21:18Z",
 "arbiter#9": "2026-07-14T18:49:15Z",
 "dispatcher#5": "2026-07-14T18:48:58Z",
 "applications#25": "2026-07-14T18:48:52Z",
 "docs#1": "2026-07-09T20:35:14Z",
 "applications#8": "2026-04-05T22:08:47Z",
 "applications#4": "2026-02-26T15:40:27Z",
}
for k,v in times.items():
    t = datetime.strptime(v, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
    diff = (now - t).total_seconds()/3600
    print(k, round(diff), "h")
