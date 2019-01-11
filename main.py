import datetime
import time
from nokiahealthapi import get_meas, get_sleep, get_summary
from myapi import read_nokiahealthapi_tokens, create_body_measures, create_sleep_series, create_sleep_summary

members = []

now = datetime.datetime.now()
now_unixtime = int(time.mktime(now.timetuple()))

a_day_to_seconds = 86400

startdate = now_unixtime - a_day_to_seconds
enddate = now_unixtime

today = datetime.date.today()

for member in members:
    nokiahealthapi_tokens = read_nokiahealthapi_tokens(member)
    access_token = nokiahealthapi_tokens["access_token"]

    body_measures = get_meas(access_token, startdate, enddate)

    if body_measures["status"] == 0:
        if body_measures["body"]["measuregrps"] != []:
            create_body_measures(body_measures["body"]["measuregrps"], member)
        else:
            print("no body_measures dara")
    else:
        print("status %s" % body_measures["status"])

    sleep = get_sleep(access_token, startdate, enddate)

    if sleep["status"] == 0:
        if sleep["body"]["series"] != []:
                create_sleep_series(sleep["body"]["series"], member, now_unixtime)
        else:
            print("no sleep_series dara")
    else:
        print("status %s" % sleep["status"])

    sleep_summary = get_summary(access_token, today.isoformat(), today.isoformat())

    if sleep_summary["status"] == 0:
        if sleep_summary["body"]["series"] != []:
                    create_sleep_summary(sleep_summary["body"]["series"], member)
        else:
            print("no sleep_series dara")
    else:
        print("status %s" % sleep_summary["status"])