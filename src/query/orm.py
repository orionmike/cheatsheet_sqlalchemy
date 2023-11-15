from sqlalchemy import select
from database import Base, sync_engine, sync_session_maker
from models import Object


def recreate_all_table():
    sync_engine.echo = False
    try:
        Base.metadata.drop_all(sync_engine)
    except:
        pass
    Base.metadata.create_all(sync_engine)
    sync_engine.echo = True


def insert_object():
    with sync_session_maker() as session:
        object_1 = Object(name="object_1")
        object_2 = Object(name="object_1")
        session.add_all([object_1, object_2])
        # flush отправляет запрос в базу данных
        # После flush каждый из работников получает первичный ключ id, который отдала БД
        session.flush()
        session.commit()


def get_object():

    with sync_session_maker() as session:
        obj = select(Object).filter_by(id_object=123).first()
        obj = session.query(Object).filter(Object.id_object == 123).first()
        obj = session.query(Object).filter_by(id_object=123).first()
        session.commint()

    return obj


def select_object_list():

    with sync_session_maker() as session:
        object_list = select(Object).filter(Object.id_object > 10).all()
        object_list = session.query(Object).filter(Object.id_object > 10).all()
        object_list = session.query(Object).filter_by(id_object=123).all()

        session.commint()

    return object_list


def delete_object():

    with sync_session_maker() as session:

        obj = session.query(Object).filter_by(id_object=123).first()
        session.delete(obj)

        obj_list = session.query(Object).filter_by(id_object=123).all()
        session.delete(obj_list)

        obj_list = session.query(Object).filter_by(id_object=123).delete()
        session.commit()
