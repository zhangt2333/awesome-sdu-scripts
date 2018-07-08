# -*- coding: utf-8 -*-
#!/usr/bin/env python
# Copyright 2018 ZhangT. All Rights Reserved.
# Author: ZhangT
# Author-Github: github.com/zhangt2333
# config.py 2018/7/8 19:41

import hashlib

HEADERS = { "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Encoding":"gzip, deflate, sdch",
            "Accept-Language":"zh-CN,zh;q=0.8",
            "Connection":"keep-alive",
            "Host":"bkjwxk.sdu.edu.cn",
            "Referer":"http://www.bkjx.sdu.edu.cn/",
            "Upgrade-Insecure-Requests":"1",
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"}

Cookies = {'JSESSIONID': '',
           'sduxk': ''
           # 'j_username': '',
           # 'j_password': '',
           # 'index': '0'
          }


def generateMD5(str):
    """工具函数：对字符串进行md5编码"""
    hl = hashlib.md5()
    hl.update(str.encode(encoding='utf-8'))
    return hl.hexdigest()

