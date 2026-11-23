from telethon import TelegramClient, events


API_ID = 32667476
API_HASH = "" # di my.telegram.org > api developmen
BOT = "@.."   # username bot atau chat id

client = TelegramClient("sesi_saya", API_ID, API_HASH)

@client.on(events.NewMessage(chats=BOT))
async def handler(event):
    arah = "saya" if event.out else "bot"
    print(arah, ":", event.raw_text)

    if arah == "bot":
        with open("/tmp/captcha_service.txt", "w") as out:
            out.write(f"{event.raw_text}")

client.start()
client.run_until_disconnected()
