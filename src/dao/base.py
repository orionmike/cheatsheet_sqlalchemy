

from database import Base, sync_engine, sync_session_maker
from models import Object


class BaseDAO:
    model = None
