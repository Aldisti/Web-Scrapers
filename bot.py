from pyrogram import Client, filters
from time import sleep
import test

app = Client(
    "B0BB0BOT",
    api_id = 7775230,
    api_hash = "9969d92d115b3941a78ef9001aefdf50",
    bot_token = "2089459247:AAG0UVBUr3Vdf8syrjg413gUJH4KPsdQjfM"
)

with app:
    app.send_message("Aldisti0", "Bot is ready to use")

@app.on_message(filters.private & filters.command('check', prefixes=['/', '.', ';', '>', '#'], case_sensitive=False))
async def check(client, message):
    await message.reply_text("Bot is turning on...")
    while True:
        test.main(app)
        sleep(15)

@app.on_message(filters.private & filters.command(['st', 'shutdown', 'stop'], prefixes=['/', '.', ';', '>', '#'], case_sensitive=False))
async def shutdown(client, message):
    await message.reply_text("Bot is shutting down...")
    quit()

app.run()