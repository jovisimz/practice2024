
from cfg import API_TOKEN
from cfg import API_HASH
from cfg import API_ID
from cfg import CHANNEL
from cfg import FORWARD_TO

from telethon import TelegramClient, events

practice_bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=API_TOKEN)

@practice_bot.on(events.NewMessage(pattern='/start'))
async def start(event):
    await event.respond('Привет, вывод доп информации командой /info')

@practice_bot.on(events.NewMessage(pattern='/info'))
async def start(event):
    await event.respond('¯\_(ツ)_/¯')

@practice_bot.on(events.NewMessage(chats=CHANNEL))
async def handler(event):
    await practice_bot.forward_messages(FORWARD_TO, event.message)

practice_bot.start()
practice_bot.run_until_disconnected()
