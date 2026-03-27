import discord
import subprocess
import asyncio
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

client = discord.Client(intents=discord.Intents.default())


async def get_reminders():
    loop = asyncio.get_event_loop()
    result = await loop.run_in_executor(None, lambda: subprocess.run(
        ["osascript", "-e",
         'tell application "Reminders" to get name of (reminders of list "미리 알림" whose completed is false)'],
        capture_output=True, text=True
    ))
    if result.returncode != 0:
        return []
    return result.stdout.strip().split(", ")

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    user = await client.fetch_user(400163520374898688)
    reminders = await get_reminders()
    message = "오늘 할 일 목록:\n" + "\n".join(f"- {r}" for r in reminders)
    await user.send(message)
    await user.send("오늘하루도 화이팅!")
    await client.close()

client.run(TOKEN)