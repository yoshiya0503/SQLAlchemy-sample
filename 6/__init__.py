#! /usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
__init_-.py
test
"""
__author__ = 'Yoshiya Ito <myon53@gmail.com>'
__version__ = '0.0.1'
__date__ = '24 10 2015'


from sqlalchemy.orm import sessionmaker
from models import *
from schemas import *

Session = sessionmaker()
session = Session()
metadata.create_all()
r0 = Region(name='NorthEast')
r1 = Region(name='NorthWest')
print(r0, r1)

s = Synonym()
s.status = 'test'
print(s.status)

session.add_all([r0, r1, s])
session.commit()
print('##################')
print(r0.id)
print(r0.name)
