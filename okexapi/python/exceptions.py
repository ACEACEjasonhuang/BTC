# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :BTC 
# @File     :exceptions
# @Date     :2023/3/12 0012 16:46 
# @Author   :Junzhe Huang
# @Email    :acejasonhuang@163.com
# @Software :PyCharm
-------------------------------------------------
"""


class OKXServerError(Exception):
    """
    Base exception for server-side errors
    HTTP code 5.x.x
    Exception return args:
    - HTTP Status Code
    - Response Text
    """


class OKXClientError(Exception):
    """
    Base exception for client-side errors
    HTTP code 4.x.x
    Exception return args:
    - HTTP Status Code
    - Response Text
    """


class OKXContentException(Exception):
    """
    Base exception for successful API responses that
    return a success code > 0
    Exception return args:
    - OKX error code
    - OKX error message
    - Original Request
    - Response JSON
    """