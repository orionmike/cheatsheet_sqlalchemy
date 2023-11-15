from sqlalchemy import create_engine

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from config import *

async_engine = create_async_engine(URL_OBJECT_ASYNC)
async_session_maker = sessionmaker(async_engine, class_=AsyncSession, expire_on_commit=False)

sync_engine = create_engine(URL_OBJECT_SYNC)
sync_session_maker = sessionmaker(sync_engine, expire_on_commit=False)


class Base(DeclarativeBase):
    pass


if __name__ == '__main__':
    Base.metadata.create_all(sync_engine)
