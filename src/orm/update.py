from sqlalchemy import update
from database import sync_session_maker
from models import Object


def update_object() -> None:

    with sync_session_maker() as session:
        session.query(Object).filter(Object.id_object == 123).update(
            Object.name == 'new_name'
        )
        session.commit()

    with sync_session_maker() as session:
        query = update(Object).filter(Object.id_object == 123).values(name='new_name')
        session.execute(query)
        session.commit()
