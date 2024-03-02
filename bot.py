from pyrogram import Client, filters

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
bot_token = '6991774790:AAFjhJM3Gi_aNYhpV6XQ6_zMNusu9F0CevU'

# Create a Pyrogram Client
app = Client('my_user_id_bot', bot_token=bot_token)

# Define a handler for the /getid command
@app.on_message(filters.command("getid", prefixes="/"))
def get_user_id(client, message):
    user_id = message.from_user.id
    message.reply_text(f"Your User ID is: {user_id}")

# Run the bot
if __name__ == "__main__":
    app.run()
