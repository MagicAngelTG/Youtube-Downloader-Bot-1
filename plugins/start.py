from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Update Channel", url="https://t.me/x_botz"),
         InlineKeyboardButton("Support Group", url="https://t.me/x_botzz")
         ],
         [
         InlineKeyboardButton("Developer", url="https://t.me/Akfronic"),
         InlineKeyboardButton("Share", url="https://t.me/share/url?url=Join%20%40X_Botz")]])
    welcomed = f"Hai <b>{message.from_user.mention}, \n\n**Iam a Youtube Video Downloader Bot. Send Me Any YouTube Video Link I Will Upload To Telegram With Custum Thumbnail Support\n\nFor More Details Press** /help\n\n**⚜️ Maintained By : @X_Botz**"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
