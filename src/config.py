
from datetime import datetime
import sys
from sqlalchemy.engine import URL
from pathlib import Path


# ABS_PATH = ''  # for win
# ABS_PATH = f'{sys.path[0]}/app/'  # for linux

ABS_PATH = Path(__file__).parent.resolve()
APP_NAME = 'sqlalchemy cheatsheet'


# =====================================
# load config

try:

    if sys.version_info.major == 3 and sys.version_info.minor >= 11:

        import tomllib

        with open(f"{ABS_PATH}/config.toml", "rb") as f:
            config = tomllib.load(f)
    else:

        import toml

        with open(f"{ABS_PATH}/config.toml", "r") as f:
            config = toml.load(f)

    IND = config['utils']['console_indent']

    # async case
    URL_OBJECT_ASYNC = URL.create(
        "postgresql+asyncpg",
        username=config['db']['db_user'],
        password=config['db']['db_password'],
        host=config['db']['host'],
        database=config['db']['db_name']
    )

    # sync case
    URL_OBJECT_SYNC = URL.create(
        "postgresql",
        username=config['db']['db_user'],
        password=config['db']['db_password'],
        host=config['db']['host'],
        database=config['db']['db_name']
    )

    # sqlite

    # engine = create_engine("sqlite://") in memory

    URL_SQLITE = URL.create(
        f"sqlite:////{ABS_PATH}/{config['db_sqlite']['db_dir']}/{config['db_sqlite']['db_file']}"
    )

    print(f'{datetime.now()} start app: {APP_NAME}')
    # print(f'{IND} python {sys.version_info.major}.{sys.version_info.minor}')
    # print(f'{IND} config loaded: OK')

except Exception as e:
    raise Exception(f'config load -> error: {e}')
