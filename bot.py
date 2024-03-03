from telethon import TelegramClient, events

# Replace with your own values
api_id = 15191874
api_hash = '3037d39233c6fad9b80d83bb8a339a07'
bot_token = 6991774790:'AAFsYGdXqc7gvxruvklWESj9KPUG3DGOBjA'

async def main():
    async with TelegramClient('my_bot', api_id, api_hash) as client:
        @client.on(events.NewMessage(pattern='/start'))
        async def handle_start(event):
            await event.reply('Hello!  This is a simple bot.')

        @client.on(events.NewMessage)
        async def handle_message(event):
            await event.reply(f'You said: {event.text}')

        # Start the client and wait for events
        await client.start()
        await client.run_until_disconnected()

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
