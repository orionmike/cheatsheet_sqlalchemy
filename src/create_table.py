

from database import Base, sync_engine, file_engine
from models import Object, TagObject, CategoryObject


def recreate_table_list(table_list, engine):
    for model in table_list:
        try:
            model.__table__.drop(engine)
        except:
            pass
    Base.metadata.create_all(engine)


if __name__ == '__main__':
    # Base.metadata.create_all(file_engine)
    recreate_table_list([Object, TagObject, CategoryObject], file_engine)
