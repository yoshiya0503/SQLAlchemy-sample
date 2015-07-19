from sqlalchemy import *
from datetime import datetime
from sqlalchemy.orm import *


metadata = MetaData('mysql+pymysql://root:root@localhost/tutorial')
metadata.bind.echo = True


user_table = Table(
    'tf_user', metadata,
    Column('id', Integer, primary_key=True),
    Column('user_name', Unicode(16), unique=True, nullable=False),
    Column('password', Unicode(40), nullable=False),
    Column('display_name', Unicode(255), default=''),
    Column('created', DateTime, default=datetime.now())
)

group_table = Table(
    'tf_group', metadata,
    Column('id', Integer, primary_key=True),
    Column('group_name', Unicode(16), unique=True, nullable=False),
)

permission_table = Table(
    'tf_permission', metadata,
    Column('id', Integer, primary_key=True),
    Column('permission_name', Unicode(16), unique=True, nullable=False)
)

user_group_table = Table(
    'tf_user_group', metadata,
    Column('user_id', None, ForeignKey('tf_user.id'), primary_key=True),
    Column('group_id', None, ForeignKey('tf_group.id'), primary_key=True)
)

group_permission_table = Table(
    'tf_group_permission', metadata,
    Column('permission_id', None, ForeignKey('tf_permission.id'), primary_key=True),
    Column('group_id', None, ForeignKey('tf_group.id'), primary_key=True)
)


metadata.create_all()

class User(object): pass
class Group(object): pass
class Permission(object): pass

mapper(User, user_table)
mapper(Group, group_table)
mapper(Permission, permission_table)

if __name__ == '__main__':

    """
    接続は一回でコネクションプーリングを用いているが、
    DBへのラウンドトリップは多いパターン
    executeのたびにアクセスする(executeするたびにcommitする)
    """
    user_table.delete().execute()

    user_table.insert().execute(user_name='rick1', password='secret', display_name='rick C')
    user_table.insert().execute(user_name='rick2', password='secret', display_name='rick C')
    for row in user_table.select().execute():
        print(row)

    result = user_table.select().execute()
    row = result.fetchone()
    print(row['user_name'])

    """
    変更をsessionにキャッシュしておき、すべてsessionを見ると参照できる
    こちらはDBへのラウンドトリップが一回
    """
    print("##############################")
    Session = sessionmaker()
    session = Session()
    # queryを用いるとDBへアクセスする
    # sessionは自動的にDBへフラッシュする機能がある
    query = session.query(User)
    print(list(query))
    for user in query:
        print(user.user_name)

    for user in query.filter(User.user_name.like("rick%")):
        print('({0}, {1}, {2})'.format(user.id, user.user_name, user.created))

    newuser = User()
    newuser.user_name = 'yoshiya'
    newuser.password = 'hoge'
    session.add(newuser)
    print("#################")

    # auto flush
    for user in query:
        print(user.user_name)
