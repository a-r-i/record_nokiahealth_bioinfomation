# from config import NOKIAHEALTHAPI_CLIENT_ID, NOKIAHEALTHAPI_CLIENT_SECRET
from config_heroku import NOKIAHEALTHAPI_CLIENT_ID, NOKIAHEALTHAPI_CLIENT_SECRET
from myapi import read_nokiahealthapi_tokens, update_nokiahealthapi_tokens
from nokiahealthapi import refresh_accesstoken

members = []

for member in members:
    nokiahealthapi_tokens = read_nokiahealthapi_tokens(member)
    refresh_token = nokiahealthapi_tokens["refresh_token"]

    r_json = refresh_accesstoken(NOKIAHEALTHAPI_CLIENT_ID, NOKIAHEALTHAPI_CLIENT_SECRET, refresh_token)

    update_nokiahealthapi_tokens(member, r_json["access_token"], r_json["refresh_token"])