#! /usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
DML.py
"""
__author__ = 'Yoshiya Ito <myon53@gmail.com>'
__version__ = '0.0.1'
__date__ = '13 Oct 2015'
import sqlalchemy as sa
from sqlalchemy import MetaData, Table, Column, Integer, String, ForeignKey, intersect
from sqlalchemy import create_engine, bindparam

if __name__ == '__main__':

    metadata = MetaData()

    simple_table = Table('simple', metadata,
                         Column('id', Integer, primary_key=True),
                         Column('col1', String(20))
                         )
    second_table = Table('second', metadata,
                         Column('id', Integer, primary_key=True),
                         Column('simple_id', Integer, ForeignKey('simple.id'), primary_key=True),
                         )
    stmt = simple_table.insert()
    print(stmt)
    print(stmt.compile().params)

    # engine bind
    engine = create_engine('mysql+pymysql://root:@localhost:3306/tutorial')
    #simple_table.delete(bind=engine).execute()
    #second_table.create(bind=engine)
    # create は テーブルを作成する
    #simple_table.create(bind=engine)
    #engine.execute(stmt, col1='Foo')
    metadata.bind = engine
    stmt = simple_table.insert(values=dict(col1='new data'))
    #stmt.execute()
    print(stmt.compile().params)

    # multi insert , stmt -> metadata -> engine
    #stmt.execute([dict(col1='1'), dict(col1='2'), dict(col1='3')])

    # update
    stmt = simple_table.update(
        whereclause="id=2",
        values=dict(col1='update data')
    )
    print(stmt)
    #stmt.execute()
    # delete
    stmt = simple_table.delete(whereclause="id='18'")
    print(stmt)
    #stmt.execute()

    # select
    #stmt = simple_table.select(whereclause='id="8"')
    print('============================')
    stmt = simple_table.select(simple_table.c.id=='7')
    print(stmt)
    print(stmt.execute().fetchone())
    stmt = simple_table.select(simple_table.c.col1!='update data')
    print(stmt.execute().fetchall())
    print(stmt.execute().rowcount)

    # bindparam
    print('============================')
    stmt = simple_table.select(whereclause=simple_table.c.id==bindparam('id'))
    print(stmt.execute(id=6).fetchone())
    stmt = simple_table.select(group_by=[simple_table.c.col1])
    print(stmt.execute().fetchall())

    print('============================')
    # join
    from_obj = simple_table.join(second_table)
    #from_obj = simple_table.outerjoin(second_table)
    q = simple_table.select().select_from(from_obj).where(simple_table.c.id == second_table.c.simple_id)
    print(q.column('second.simple_id'))
    print(q.execute().fetchall())

    # set operation
    print('============================')
    q1 = simple_table.select(simple_table.c.id > 1)
    q2 = simple_table.select(simple_table.c.id < 7)
    print(q1.execute().fetchall())
    print(q2.execute().fetchall())
    q = intersect(q1, q2)
    print(q)
