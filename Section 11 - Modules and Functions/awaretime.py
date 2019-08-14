import datetime
import pytz

local_time = datetime.datetime.now()
utc_time = datetime.datetime.utcnow()

print("Naive local time {}".format(local_time))
print("Naive UTC {}".format(utc_time))

aware_local_time = pytz.utc.localize(local_time).astimezone()
aware_utc_time = pytz.utc.localize(utc_time)

print("Aware locla time {}, time zone {}".format(aware_local_time, aware_local_time.tzinfo))
print("Aware utc time {} time zone {}".format(aware_utc_time, aware_utc_time.tzinfo))