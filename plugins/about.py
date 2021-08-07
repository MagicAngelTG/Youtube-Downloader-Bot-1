from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["about"]))
async def start(client, message):

    about = "• **Bot :** YouTube DL \n\n• **Channel :** @X_Botz \n\n• **Language :** Python \n\n• **Framework :** Pyrogram"
    await message.reply_text(about)
