from sqlalchemy.ext.asyncio import AsyncSession

from models.users import Users
# from querysets.products import get_products_qs


async def insert_user(session: AsyncSession, user_instance: Users) -> None:
    """Добавление нового пользователя в базу"""
    session.add(user_instance)
    await session.commit()


async def is_user_exists(session: AsyncSession, user_id: int) -> bool:
    user = await session.get(Users, user_id)
    return user is not None
