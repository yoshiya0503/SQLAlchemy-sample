#! /usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
__init__
継承テスト
"""
__author__ = 'Yoshiya Ito <myon53@gmail.com>'
__version__ = '0.0.1'
__date__ = '31 Oct 2015'
from models import *
from schemas import *

session = Session()
metadata.create_all()

products = [
    Product('111', 1223),
    Product('222', 1223),
    Clothing('333', 1223, 'clothing'),
    Clothing('444', 1223, 'clothing'),
    Accessory('555', 1223, 'accessory'),
    Accessory('666', 1223, 'accessory'),
]

#session.add_all(products)
#session.commit()
