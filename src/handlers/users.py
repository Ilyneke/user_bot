from sqlalchemy.ext.asyncio import AsyncSession
from pyrogram.types import Message

from methods.users import is_user_exists, insert_user
from models.users import Users


async def message_handler(client, message: Message, session: AsyncSession):
    user_id = message.from_user.id

    if not await is_user_exists(session=session, user_id=user_id):
        await insert_user(session=session, user_instance=Users(id=user_id))
    else:
        pass

    await message.reply(message.text)
