import requests


TOKEN = "8998193648:AAHA44XtSIp8LV-yjMLsT0QpnNA4NM1ZdF8"
CHAT_ID = 7797309176


import requests
import time

API = f"https://api.telegram.org/bot{TOKEN}"

# Kirim pesan
r = requests.post(API + "/sendMessage", data={
    "chat_id": CHAT_ID,
    "text": "Halo, apakah kamu menerima pesan ini?"
})

print("SEND:", r.json())

# Baca balasan
offset = 0

while True:
    data = requests.get(API + "/getUpdates", params={
        "offset": offset,
        "timeout": 30,
        "allowed_updates": '["message"]'
    }, timeout=40).json()

    for update in data.get("result", []):
        offset = update["update_id"] + 1

        msg = update.get("message", {})
        chat_id = str(msg.get("chat", {}).get("id", ""))

        if chat_id == str(CHAT_ID):
            text = msg.get("text", "")
            print("BALASAN:", text)

    time.sleep(1)
