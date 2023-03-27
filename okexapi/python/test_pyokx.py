# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :BTC 
# @File     :test_pyokx
# @Date     :2023/3/12 0012 21:05 
# @Author   :Junzhe Huang
# @Email    :acejasonhuang@163.com
# @Software :PyCharm
-------------------------------------------------
"""
import os

# python-dotenv should have been installed from the dependencies
from dotenv import load_dotenv
from api_base import OKXClient
from marketdata_api import MarketData

# read information from .env file
load_dotenv()

# create the base client:
client = OKXClient(
    key=os.getenv('KEY'),
    secret=os.getenv('SECRET'),
    passphrase=os.getenv('PASSPHRASE'),
    proxies={
        'http': 'http://47.57.188.208:80',
        'https': 'http://47.57.188.208:80'
    }
)

mkd = MarketData(client)

print(mkd.get_order_book('BTC-USDT', use_proxy=True))