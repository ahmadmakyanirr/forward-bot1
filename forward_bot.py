import os
import base64
from telethon import TelegramClient, events

# Environment variables
api_id = int(os.environ.get("API_ID"))
api_hash = os.environ.get("API_HASH")
session_str = os.environ.get("SESSION_STR")
source_channel = int(os.environ.get("SOURCE_ID"))
target_chat = int(os.environ.get("TARGET_ID"))

# Decode session string to file
if not session_str:
    raise Exception("SESSION_STR متغیر محیطی تنظیم نشده!")
with open("mybot.session", "wb") as f:
    f.write(base64.b64decode(session_str))

# Run client
client = TelegramClient("mybot.session", api_id, api_hash)

@client.on(events.NewMessage(chats=source_channel))
async def handler(event):
    print("پیام دریافت شد:", event.message.text)
    await client.send_message(target_chat, event.message)

print("🚀 ربات اجرا شد و منتظر پیام است...")
client.start()
client.run_until_disconnected()