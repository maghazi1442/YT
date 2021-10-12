from datetime import datetime, timedelta
from pyrogram import Client, Filters, InlineKeyboardMarkup, InlineKeyboardButton
from bot import user_time
from config import youtube_next_fetch
from helper.ytdlfunc import extractYt, create_buttons
import wget
import os
from PIL import Image

ytregex = r"^((?:https?:)?\/\/)?((?:www|m)\.)?((?:youtube\.com|youtu.be))(\/(?:[\w\-]+\?v=|embed\/|v\/)?)([\w\-]+)(\S+)?$"


@Client.on_message(Filters.regex(ytregex))
async def ytdl(_, message):
    userLastDownloadTime = user_time.get(message.chat.id)
    try:
        if userLastDownloadTime > datetime.now():
            wait_time = round((userLastDownloadTime - datetime.now()).total_seconds() / 60, 2)
            await message.reply_text(f"`Sabar menunggu ikhwah {wait_time} Beberapa menit`")
            return
    except:
        pass

    url = message.text.strip()
    await message.reply_chat_action("typing")
    try:
        title, thumbnail_url, formats = extractYt(url)

        now = datetime.now()
        user_time[message.chat.id] = now + \
                                     timedelta(minutes=youtube_next_fetch)

    except Exception:
        await message.reply_text("`Failed To Fetch Youtube Data...  \nPossible Youtube Blocked server ip \n#error`")
        return
    buttons = InlineKeyboardMarkup(list(create_buttons(formats)))
    sentm = await message.reply_text("Sedang proses mengecek url ....")
    try:
        # Todo add webp image support in thumbnail by default not supported by pyrogram
        # https://www.youtube.com/watch?v=lTTajzrSkCw
        img = wget.download(thumbnail_url)
        im = Image.open(img).convert("RGB")
        output_directory = os.path.join(os.getcwd(), "downloads", str(message.chat.id))
        if not os.path.isdir(output_directory):
            os.makedirs(output_directory)
        thumb_image_path = f"{output_directory}.jpg"
        im.save(thumb_image_path,"jpeg")
        await message.reply_photo(thumb_image_path, caption=title, reply_markup=buttons)
        await sentm.delete()
    except Exception as e:
        print(e)
        try:
            thumbnail_url = "https://telegra.ph/file/fe9fa32a8906e5962b3d5.jpg"
            await message.reply_photo(thumbnail_url, caption=title, reply_markup=buttons)
        except Exception as e:
            await sentm.edit(
            f"<code>{e}</code> #Error")

