from pyrogram import Client, filters
from pyrogram.handlers import MessageHandler

from handlers.users import message_handler
from settings.base import API_ID, API_HASH


app = Client("nu_i_dela", api_id=API_ID, api_hash=API_HASH)


_message_handler = MessageHandler(message_handler, filters=[filters.text & filters.private])


app.run()  # Automatically start() and idle()
