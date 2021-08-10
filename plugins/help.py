from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"kirim link video youtube bot ini, insya' Allah kami akan mengunduh"
    await message.reply_text(helptxt)
