from sqlalchemy import create_engine

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from config import *

async_engine = create_async_engine(URL_OBJECT_ASYNC)
async_session_maker = sessionmaker(async_engine, class_=AsyncSession, expire_on_commit=False)

sync_engine = create_engine(URL_OBJECT_SYNC)
sync_session_maker = sessionmaker(sync_engine, expire_on_commit=False)


print(DB_FILE)

file_engine = create_engine(f"sqlite:////{DB_FILE}")
file_session_maker = sessionmaker(file_engine)


class Base(DeclarativeBase):
    pass


def recreate_all_table(engine) -> None:
    sync_engine.echo = False
    try:
        Base.metadata.drop_all(engine)
    except:
        pass
    Base.metadata.create_all(engine)
    sync_engine.echo = True


if __name__ == '__main__':
    print(DB_FILE)
    Base.metadata.create_all(file_engine)
