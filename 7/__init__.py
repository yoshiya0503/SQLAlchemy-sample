#! /usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
__init__.py
sessionの挙動確認
"""
__author__ = 'Yoshiya Ito <myon53@gmail.com>'
__version__ = '0.0.1'
__date__ = '29 10 2015'
from models import *
from schemas import *
from sqlalchemy import event


@event.listens_for(Product, 'load')
def show_status(target, value):
    print('LOAD DATA: product')

@event.listens_for(Product, 'before_update')
def show_status2(target, value, ini):
    print('BEFORE UPDATE: product')

@event.listens_for(Product.msrp, 'set', named=True)
def shoq_status3(**kw):
    print('set new value')


session = Session()

p1 = session.query(Product).filter_by(sku=101).one()
p2 = session.query(Product).filter_by(sku=502).one()
p2 = session.query(Product).get(502)
print(p2.sku)
#p1 = Product(sku=102, msrp=111)
#p2 = Product(sku=505, msrp=121)
p1.msrp -= 100
session.add(p1)
session.commit()

q = session.query(Product).outerjoin('categories').all()
print(q)

"""
session.add(p1)
session.add(p2)
session.delete(p1)
session.delete(p2)
session.commit()
"""
