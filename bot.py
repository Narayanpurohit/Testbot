from telethon.sync import TelegramClient, events

bot_token = '6991774790:AAFjhJM3Gi_aNYhpV6XQ6_zMNusu9F0CevU'

client = TelegramClient('bot_session', bot_token=bot_token)

@client.on(events.NewMessage(pattern='/start'))
async def handler(event):
    await event.respond('Hello! I am your bot.')

@client.on(events.NewMessage)
async def echo(event):
    await event.respond(event.text)

if __name__ == '__main__':
    client.start()
    client.run_until_disconnected()
