import requests

def refresh_accesstoken(client_id, client_secret, refresh_token):
    url = "https://account.withings.com/oauth2/token"

    payload = {
                "grant_type": "refresh_token",
                "client_id": client_id,
                "client_secret": client_secret,
                "refresh_token": refresh_token
              }

    r = requests.post(url, data=payload)

    return r.json()

def get_meas(access_token, startdate, enddate):
    url = "https://wbsapi.withings.net/measure?action=getmeas"

    payload = {
                "access_token": access_token,
                "startdate": startdate,
                "enddate": enddate
              }

    r = requests.get(url, params=payload)

    return r.json()

def get_sleep(access_token, startdate, enddate):
    url = "https://wbsapi.withings.net/v2/sleep?action=get"

    payload = {
               "access_token": access_token,
               "startdate": startdate,
               "enddate": enddate
              }

    r = requests.get(url, params=payload)

    return r.json()

def get_summary(access_token, startdateymd, enddateymd):
    url = "https://wbsapi.withings.net/v2/sleep?action=getsummary"

    payload = {
               "access_token": access_token,
               "startdateymd": startdateymd,
               "enddateymd":enddateymd
              }

    r = requests.get(url, params=payload)

    return r.json()