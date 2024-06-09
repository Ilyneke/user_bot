import asyncio

from pyrogram import Client
from pyrogram.types import Message
from pyrogram.errors import UserDeactivated, UserBlocked

from methods.users import change_user_status
from settings.db import async_session


async def check_triggers(client: Client, message: Message, queries: list | str) -> bool:
    me = await client.get_me()
    user_id = message.from_user.id
    if isinstance(queries, str):
        queries = [queries]
    for query in queries:
        if await client.search_messages_count(chat_id=user_id, query=query, from_user=me.id) != 0:
            return False
    return True


def get_messages():
    for message in [(6, 'Текст1', None), (39, 'Текст2', 'Триггер1'), (26 * 60, 'Текст3', None)]:
        yield message


async def send_messages(client: Client, message: Message) -> None:
    messages = get_messages()
    user_id = message.from_user.id
    while True:
        async with async_session() as session:
            # берем следующее сообщение
            try:
                time, text, trigger = next(messages)
            except StopIteration:
                await change_user_status(session=session, user_id=user_id, status='finished')
                break

            # ставим паузу согласно времени в сообщении
            await asyncio.sleep(time * 60)

            # проверяем не было ли от нас следующих слов в диалоге
            trigger_queries = ['прекрасно', 'ожидать']
            if not await check_triggers(client=client, message=message, queries=trigger_queries):
                break

            # если у сообщения есть тригер, то проверяем
            if trigger is not None:
                if not await check_triggers(client=client, message=message, queries=trigger):
                    # если нашлось то переходим к следующему сообщению
                    time, text, trigger = next(messages)

            try:
                await client.send_message(chat_id=message.from_user.id, text=text)
            except (UserDeactivated, UserBlocked):
                await change_user_status(session=session, user_id=user_id, status='dead')
                break
