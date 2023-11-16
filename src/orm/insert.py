
from database import sync_session_maker
from models import Object
from sqlalchemy import insert


def insert_object() -> None:
    with sync_session_maker() as session:
        object_1 = Object(name="object_1")
        session.add(object_1)

        object_2 = Object(name="object_2")
        session.add_all([object_1, object_2])

        # flush отправляет запрос в базу данных
        # После flush каждый из работников получает первичный ключ id, который отдала БД
        session.flush()

        session.commit()

    with sync_session_maker() as session:
        query = insert(Object).values(name="spongebob")
        session.execute(query)

        # work with dict
        objects = [
            {"name": "object_1"},
            {"name": "object_2"},
            {"name": "object_3"},
        ]

        query = insert(Object).values(objects)
        session.execute(query)
        session.commit()
