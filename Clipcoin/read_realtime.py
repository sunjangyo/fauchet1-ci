import os
from telethon import TelegramClient, events

API_ID = 32667476
API_HASH = ""
BOT = "@sunjangyo12bot"


client = TelegramClient("sesi_saya", API_ID, API_HASH)

def tampil(m):
    arah = "saya" if m.out else "bot "
    teks = m.raw_text or "[media/tanpa teks]"
    print(f"{m.date.astimezone().strftime('%Y-%m-%d %H:%M')} {arah}: {teks}")

def simpan_captcha(m):
    if not m.out:
        with open("/tmp/captcha_service.txt", "w") as f:
            f.write(m.raw_text or "")

@client.on(events.NewMessage(chats=BOT))
async def baru(event):
    tampil(event.message)
    simpan_captcha(event.message)

async def main():
    await client.start()

    terakhir_bot = None
    # SEMUA riwayat, urut lama -> baru, langsung tampil saat dijalankan
    async for m in client.iter_messages(BOT, limit=10):
        tampil(m)
        if not m.out:
            terakhir_bot = m
            break

    # simpan pesan bot paling baru ke file
    if terakhir_bot:
        simpan_captcha(terakhir_bot)

    print("--- riwayat selesai, memantau pesan baru ---")
    await client.run_until_disconnected()

client.loop.run_until_complete(main())
