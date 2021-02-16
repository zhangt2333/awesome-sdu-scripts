# -*- coding: utf-8 -*-
# !/usr/bin/env python
# Copyright 2021 zhangt2333. All Rights Reserved.
# Author-Github: github.com/zhangt2333
# uniform_login_spider.py 2021/2/13 21:27

import requests
import re
from . import uniform_login_des


# example: login(username='your-student-id', password='your-password', to_url='https://scenter.sdu.edu.cn/tp_fp/view')
def login(username, password, to_url):
    """登录并返回JSESSIONID"""
    url = 'https://pass.sdu.edu.cn/cas/login?service=' + to_url
    lt, execution, _eventId, JSESSIONID = getLoginCasData(url)
    HEADERS_LOGIN["Cookie"] = "JSESSIONID=" + JSESSIONID
    rsa = uniform_login_des.strEnc(username + password + lt, '1', '2', '3')
    data = dict(
        rsa=rsa,
        ul=len(username),
        pl=len(password),
        lt=lt,
        execution=execution,
        _eventId=_eventId
    )
    try:
        response = requests.post(
            url=url,
            headers=HEADERS_LOGIN,
            data=data
        )
        JSESSIONID = re.findall('<Cookie JSESSIONID=(.*?) for', str(response.request._cookies._cookies['pass.sdu.edu.cn']['/']['JSESSIONID']))[0]
        return JSESSIONID
    except execution as e:
        print(e)
        exit(-1)


def getLoginCasData(url):
    """返回CAS数据和初始JSESSIONID"""
    try:
        response = requests.get(
            url=url,
            headers=HEADERS_LOGIN
        )
        if response.status_code == 200:
            lt = re.findall('name="lt" value="(.*?)"', response.text)[0]
            execution = re.findall('name="execution" value="(.*?)"', response.text)[0]
            _eventId = re.findall('name="_eventId" value="(.*?)"', response.text)[0]
            JSESSIONID = re.findall('JSESSIONID=(.*?);', response.headers.get('set-cookie'))[0]
            return lt, execution, _eventId, JSESSIONID
    except Exception as e:
        print(e)
        exit(-1)


HEADERS_LOGIN = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Host": "pass.sdu.edu.cn",
    "Pragma": "no-cache",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36",
}
