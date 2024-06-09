from pyrogram import Client
from pyrogram.types import Message

from methods.users import is_user_exists, insert_user
from models.users import Users
from settings.db import async_session
from utils.webinar_funnel import send_messages


async def message_handler(client: Client, message: Message):
    user_id = message.from_user.id
    async with async_session() as session:
        if not await is_user_exists(session=session, user_id=user_id):
            await insert_user(session=session, user_instance=Users(id=user_id))
            await send_messages(client=client, message=message)
