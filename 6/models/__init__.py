#! /usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
__init__.py
define models
"""
__author__ = 'Yoshiya Ito <myon53@gmail.com>'
__version__ = '0.0.1'
__date__ = '24 10 2015'

from schemas import *
from sqlalchemy.orm import mapper
from sqlalchemy.ext.declarative import synonym_for
from sqlalchemy.ext import declarative
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import relationship

Base = declarative.declarative_base(metadata=metadata)


class Level(object):

    def __init__(self):
        pass


class Category(object):

    def __init__(self):
        pass


class Product(object):

    def __init__(self):
        pass


class ProductSummary(object):

    def __init__(self):
        pass


class Region(object):

    def __init__(self, name):
        self.name = name

class Store(object):

    def __init__(self, name):
        self.name = name


class Price(object):

    def __init__(self):
        pass

class Synonym(Base):
    __tablename__ = 'synonym'

    id = Column(Integer, primary_key=True)
    _status = Column('status', String(50))

    @hybrid_property
    def status(self):
        return 'the:' + self._status

    @status.setter
    def status(self, status):
        self._status = 'prefix:://' + status


mapper(Level, level_table)
mapper(Category, category_table, properties=dict(
    products=relationship(Product, secondary=product_category_table)
))
mapper(Product, product_table, properties=dict(
    categories=relationship(Category, secondary=product_category_table),
    summary=relationship(ProductSummary, uselist=False, backref='product')
))
mapper(ProductSummary, product_summary_table)
mapper(Region, region_table, properties=dict(
    stores=relationship(Store, primaryjoin=(store_table.c.region_id==region_table.c.id))
))
mapper(Store, store_table)
mapper(Price, product_price_table)
