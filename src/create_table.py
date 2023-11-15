

from database import Base, recreate_table_list, sync_engine
from models import Object, TagObject, CategoryObject


def recreate_table_list(table_list, sync_engine):
    for model in table_list:
        try:
            model.__table__.drop(sync_engine)
        except:
            pass
    Base.metadata.create_all(sync_engine)


if __name__ == '__main__':
    recreate_table_list([Object, TagObject, CategoryObject], sync_engine)
