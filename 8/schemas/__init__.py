#! /usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
__init__.py
define schema
"""
__author__ = 'Yoshiya Ito <myon53@gmail.com>'
__version__ = '0.0.1'
__date__ = '24 10 2015'

from sqlalchemy import MetaData, create_engine
from sqlalchemy import Column, Table, Integer, String, Numeric, ForeignKey, Text
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+pymysql://root:@localhost/retail')
metadata = MetaData(engine)
Session = sessionmaker(bind=engine)
STR_LEN = 20
TEXT_LEN = 255

# level table
level_table = Table(
    'level', metadata,
    Column('id', Integer, primary_key=True),
    Column('parent_id', None, ForeignKey('level.id')),
    Column('name', String(STR_LEN))
)

# category table
category_table = Table(
    'category', metadata,
    Column('id', Integer, primary_key=True),
    Column('level_id', None, ForeignKey('level.id')),
    Column('parent_id', None, ForeignKey('category.id')),
    Column('name', String(STR_LEN))
)

# product table
product_table = Table(
    'product', metadata,
    Column('sku', String(STR_LEN), primary_key=True),
    Column('msrp', Numeric),
    Column('product_type', String(1), nullable=False)
)

clothing_table = Table(
    'clothing', metadata,
    Column('sku', None, ForeignKey('product.sku'), primary_key=True),
    Column('clothing_info', String(STR_LEN))
)

accessory_table = Table(
    'accessory', metadata,
    Column('sku', None, ForeignKey('product.sku'), primary_key=True),
    Column('accessory_info', String(STR_LEN))
)

# product summary table
product_summary_table = Table(
    'product_summary', metadata,
    Column('sku', None, ForeignKey('product.sku'), primary_key=True),
    Column('name', Text(TEXT_LEN)),
    Column('description', Text(TEXT_LEN))
)

# product category table
product_category_table = Table(
    'product_category', metadata,
    Column('product_id', None, ForeignKey('product.sku'), primary_key=True),
    Column('category_id', None, ForeignKey('category.id'), primary_key=True)
)

# region table
region_table = Table(
    'region', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', Text(TEXT_LEN))
)

# store table
store_table = Table(
    'store', metadata,
    Column('id', Integer, primary_key=True),
    Column('region_id', None, ForeignKey('region.id')),
    Column('name', Text(TEXT_LEN))
)

# product price table
product_price_table = Table(
    'product_price', metadata,
    Column('sku', None, ForeignKey('product.sku'), primary_key=True),
    Column('store_id', None, ForeignKey('store.id'), primary_key=True),
    Column('price', Numeric, default=0)
)
