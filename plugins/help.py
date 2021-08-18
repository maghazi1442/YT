from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"kirim link video youtube ke bot ini, insya' Allah kami akan bantu mengunduh"
    await message.reply_text(helptxt)
