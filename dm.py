import json
import requests
import os
import time
import random
import ctypes
import selenium
import websocket
import sys
import threading

message = "YOUR_MESSAGE"

token = "YOUR_TOKEN" # be careful, it can ban your account


def DM(recipient_id, content):
    r = requests.post(
        f"https://discordapp.com/api/v9/users/@me/channels",
        headers={"authorization": token},
        json={"recipient_id": recipient_id},
    ).json()
    r2 = requests.post(
        f"https://discordapp.com/api/v9/channels/{r['id']}/messages",
        headers={
            "authorization": token,
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0",
            "accept-language": "en-US",
            "accept-encoding": "gzip, deflate, br",
            "accept": "*/*"
        },
        json={"content": content, "nonce": "", "tts": False},
    )
    print(r2.status_code)


DM('put_id_here', message)
### use it with alt account token, it bans your account really easily.
