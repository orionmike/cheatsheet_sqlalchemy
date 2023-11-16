
from database import sync_session_maker
from models import Object
from sqlalchemy import delete


def delete_object() -> None:

    with sync_session_maker() as session:

        obj = session.query(Object).filter_by(id_object=123).first()
        session.delete(obj)
        session.commit()

        obj_list = session.query(Object).filter_by(id_object=123)
        session.delete(obj_list)
        session.commit()

        obj_list = session.query(Object).filter_by(id_object=123).delete()
        session.commit()

    with sync_session_maker() as session:

        query = delete(Object).where(Object.c.name == "patrick")
        session.execute(query)
