

from database import recreate_table_list, sync_engine
from models import Object, TagObject, CategoryObject

if __name__ == '__main__':
    recreate_table_list([Object, TagObject, CategoryObject], sync_engine)
