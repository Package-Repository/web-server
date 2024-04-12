import discord
import asyncio
from threading import Thread, Event
from dotenv import load_dotenv
import os

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

client: discord.Client = discord.Client(intents=intents)

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.CustomActivity(""))
    print(f'Logged in as {client.user}')

class Bobot(Thread):
    def run(self):
        client.run(os.getenv("Token"))

_status = "online"
_activity = ""
response_event = Event()

Bobot().start()

#May need threading.Event if someone tries using ws *that* fast
async def __update_presence(status: str, message: str):
    global _status, _activity
    _status = status
    _activity = message
    await client.change_presence(status=discord.Status[status], activity=discord.CustomActivity(message))
    response_event.set()

async def __get_status():
    guild = await client.fetch_guild(972920230496067594)
    self_member = await guild.fetch_member(client.user.id)
    return client.status

async def __get_activity():
    guild = await client.fetch_guild(972920230496067594)
    self_member = await guild.fetch_member(client.user.id)
    print(self_member.activity)
    return self_member.activity

def update_status(status: str, message: str):
    response_event.clear()
    asyncio.run_coroutine_threadsafe(__update_presence(status, message), client.loop)

def get_activity() -> discord.activity.ActivityTypes | None:
    return _activity
    #return asyncio.run_coroutine_threadsafe(__get_activity(), client.loop).result()

def get_status() -> discord.Status:
    return _status
    #return asyncio.run_coroutine_threadsafe(__get_status(), client.loop).result()

def wait():
    response_event.wait()