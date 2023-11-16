from sqlalchemy import select
from database import sync_session_maker
from models import Object


def get_object() -> None:

    with sync_session_maker() as session:
        obj = select(Object).filter_by(id_object=123).first()
        obj = session.query(Object).filter(Object.id_object == 123).first()
        obj = session.query(Object).filter_by(id_object=123).first()
        obj = session.query(Object).get(1)  # get by id
        session.commit()


def select_object_list() -> None:

    with sync_session_maker() as session:
        object_list = session.query(Object).filter(Object.id_object > 10).all()
        object_list = session.query(Object).filter_by(id_object=123).all()

        session.commit()

    with sync_session_maker() as session:
        query = select(Object).filter(Object.id_object > 10).all()
        result = session.execute(query)
        object_list = result.scalars().all()
