from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"Hanya untuk kirim link video youtube"
    await message.reply_text(helptxt)
