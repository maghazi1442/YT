from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Channel", url="https://t.me/joinchat/pL-DrCapqsNiYWVh")],
        [InlineKeyboardButton(
            "Contact", url="https://t.me/joincontact")]
        [InlineKeyboardButton(
            "Contact", url="https://t.me/joincontact")]
        [InlineKeyboardButton(
            "Contact", url="https://t.me/joincontact")]
        [InlineKeyboardButton(
            "Contact", url="https://t.me/joincontact")]
        [InlineKeyboardButton(
            "Contact", url="https://t.me/joincontact")]
        [InlineKeyboardButton(
            "Contact", url="https://t.me/joincontact")]
        [InlineKeyboardButton(
            "Contact", url="https://t.me/joincontact")]
        [InlineKeyboardButton(
            "Contact", url="https://t.me/joincontact")]
        [InlineKeyboardButton(
            "Contact", url="https://t.me/joincontact")]
        [InlineKeyboardButton(
            "Contact", url="https://t.me/joincontact")]
        [InlineKeyboardButton(
            "Contact", url="https://t.me/joincontact")]
        [InlineKeyboardButton(
            "Contact", url="https://t.me/joincontact")]
        [InlineKeyboardButton(
            "Contact", url="https://t.me/joincontact")]
        [InlineKeyboardButton(
            "Contact", url="https://t.me/joincontact")]
    ])
    welcomed = f"Selamat datang di bot Annajiyah Media Center <b>{message.from_user.first_name}</b>\n/help untuk cara menggunakan"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
