from pyrogram import Client, filters
import os

# Retrieve your API ID, API hash, and bot token from environment variables
api_id = int(os.environ.get("15191874"))
api_hash = os.environ.get("3037d39233c6fad9b80d83bb8a339a07

")
bot_token = os.environ.get("6991774790:AAFjhJM3Gi_aNYhpV6XQ6_zMNusu9F0CevU")

# Create a Pyrogram Client
app = Client(
    "my_user_id_bot",
    api_id=api_id,
    api_hash=api_hash,
    bot_token=bot_token
)

# Define a handler for the /getid command
@app.on_message(filters.command("getid", prefixes="/"))
def get_user_id(client, message):
    user_id = message.from_user.id
    message.reply_text(f"Your User ID is: {user_id}")

# Run the bot
if __name__ == "__main__":
    app.run()
