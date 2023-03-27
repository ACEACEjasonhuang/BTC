# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :BTC 
# @File     :test_requests
# @Date     :2023/3/12 0012 22:38 
# @Author   :Junzhe Huang
# @Email    :acejasonhuang@163.com
# @Software :PyCharm
-------------------------------------------------
"""
import requests

response = requests.request(method='GET', url='https://www.okx.com/api/v5/market/books?instId=BTC-USDT')
print(response.json())