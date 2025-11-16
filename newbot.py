import os
import discord
import requests

# ====== تنظیمات از Environment ======
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
SOURCE_CHANNEL = int(os.getenv("SOURCE_CHANNEL"))

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
# ====================================

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

def send_to_telegram(text):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    data = {"chat_id": TELEGRAM_CHAT_ID, "text": text}
    r = requests.post(url, data=data)
    print("Telegram response:", r.status_code, r.text)

@client.event
async def on_ready():
    print("Bot is online!")

@client.event
async def on_message(message):
    if message.author.id == client.user.id:  # پیام خود ربات را نادیده بگیر
        return

    print("Message received in:", message.channel.id, "| content:", message.content)

    if message.channel.id == SOURCE_CHANNEL:
        print("Sending message to Telegram...")
        send_to_telegram(message.content)

client.run(DISCORD_TOKEN)
