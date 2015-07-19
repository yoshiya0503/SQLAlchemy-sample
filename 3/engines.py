from sqlalchemy import *
from datetime import datetime
from sqlalchemy.orm import *
import logging


if __name__ == '__main__':
    settings = {
        'echo': True,
        'echo_pool': True,
        'encoding': 'utf-8',
        'pool_size': 128,
        'strategy': 'threadlocal'
    }
    url = "mysql+pymysql://root:root@localhost/tutorial"
    engine = create_engine(url, **settings)
    handler= logging.FileHandler('sqlalchemy.log')
    handler.level = logging.DEBUG
    logging.getLogger('sqlalchemy.engine').addHandler(handler)
    logging.getLogger('sqlalchemy.pool').addHandler(handler)
    #logging.getLogger('sqlalchemy.orm').addHandler(handler)

    conn = engine.connect()
    result = conn.execute('select user_name from tf_user')
    for r in result:
        print(r)
    conn.close()
