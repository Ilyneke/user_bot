from sqlalchemy.ext.asyncio import AsyncSession

from models.users import Users


async def insert_user(session: AsyncSession, user_instance: Users) -> None:
    """Добавление нового пользователя в базу"""
    session.add(user_instance)
    await session.commit()


async def is_user_exists(session: AsyncSession, user_id: int) -> bool:
    user = await session.get(Users, user_id)
    return user is not None


async def get_user_status(session: AsyncSession, user_id: int) -> str:
    user = await session.get(Users, user_id)
    return user.status


async def change_user_status(session: AsyncSession, user_id: int, status: str) -> None:
    user = await session.get(Users, user_id)
    user.status = status
    await session.commit()
