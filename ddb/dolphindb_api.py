# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :BTC 
# @File     :dolphindb_api
# @Date     :2023/3/12 0012 3:30 
# @Author   :Junzhe Huang
# @Email    :acejasonhuang@163.com
# @Software :PyCharm
-------------------------------------------------
"""
import dolphindb as ddb


class DolphinDbApi(object):
    """
    连接dolphiindb的所有方法
    """
    def __init__(self, ip_address, port, user_name, password):
        self._s = ddb.session()
        self._s.connect(ip_address, port, user_name, password)

    def create_db(self, db_path, recreate=False):
        """

        :param db_path: 数据库路径
        :param recreate: 是否重新建立数据库
        :return:
        """