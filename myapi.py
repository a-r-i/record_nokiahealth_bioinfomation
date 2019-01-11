# from config import MYAPI_BASICAUTH_USER, MYAPI_BASICAUTH_PASS
from config_heroku import MYAPI_BASICAUTH_USER, MYAPI_BASICAUTH_PASS
import requests
import urllib

headers = {'Content-Type': 'application/x-www-form-urlencoded'}

def read_nokiahealthapi_tokens(member):
    url = "https://myapi.com/nokiahealthapi_tokens/"

    r = requests.get(
                     url=url + str(member) + '/',
                     auth=(MYAPI_BASICAUTH_USER, MYAPI_BASICAUTH_PASS)
                    )

    print(r)
    nokiahealthapi_tokens = r.json()
    return nokiahealthapi_tokens

def update_nokiahealthapi_tokens(member, access_token, refresh_token):
    url = "https://myapi.com/nokiahealthapi_tokens/"

    payload = {
                "member": member,
                "access_token": access_token,
                "refresh_token": refresh_token
              }

    r = requests.put(
                     url=url + str(member) + '/',
                     data=payload,
                     auth=(MYAPI_BASICAUTH_USER, MYAPI_BASICAUTH_PASS)
                     )
    print(r)
    return r.json()

def create_sleep_series(sleep_series, member, now_unixtime):
    url = "https://myapi.com/sleeps/"

    for series in sleep_series:
        params = {
                "member": member,
                "startdate": series["startdate"],
                "enddate": series["enddate"],
                "sleep_level": series["state"],
                "device": "Nokia Sleep"
                }
        params = urllib.parse.urlencode(params)
        requests.post(url=url, data=params, headers=headers,
                      auth=(MYAPI_BASICAUTH_USER, MYAPI_BASICAUTH_PASS))


def create_sleep_summary(sleep_summaries, member):
    url = "https://myapi/sleepsummaries/"

    for sleep_summary in sleep_summaries:
        params = {
                "member": member,
                "startdate": sleep_summary["startdate"],
                "enddate": sleep_summary["enddate"],
                 "wakeupduration": sleep_summary["data"]["wakeupduration"],
                 "lightsleepduration": sleep_summary["data"]["lightsleepduration"],
                 "deepsleepduration": sleep_summary["data"]["deepsleepduration"],
                 "remsleepduration": sleep_summary["data"]["remsleepduration"],
                 "durationtosleep": sleep_summary["data"]["durationtosleep"],
                 "durationtowakeup": sleep_summary["data"]["durationtowakeup"],
                 "wakeupcount": sleep_summary["data"]["wakeupcount"],
                "device": "Nokia Sleep"
                }
        params = urllib.parse.urlencode(params)
        requests.post(url=url, data=params, headers=headers, auth=(MYAPI_BASICAUTH_USER, MYAPI_BASICAUTH_PASS))

def create_body_measures(measuregrps, member):
    meastype = {
                76:"muscleMass",
                77:"hydration",
                88:"boneMass"
                }

    for measuregrp in measuregrps:
        url = "https://myapi.com/bodies/"
        params = {
            "timestamp": measuregrp["date"],
            "member": member,
            "muscleMass": "",
            "hydration": "",
            "boneMass": "",
            "device": "Nokia Body Plus"
        }

        for measure in measuregrp["measures"]:
            try:
                params[meastype[measure["type"]]] = measure["value"]
            except KeyError as e:
                print("type:{0}".format(type(e)))
                print("args:{0}".format(e.args))

        if not params["muscleMass"] and not params["hydration"] and not params["boneMass"]:
            print("muscleMass, hydration, boneMass is empty")
        else:
            params = urllib.parse.urlencode(params)
            requests.post(url=url, data=params, headers=headers, auth=(MYAPI_BASICAUTH_USER, MYAPI_BASICAUTH_PASS))