# -*- coding: utf-8 -*-
#!/usr/bin/env python
# Copyright 2018 ZhangT. All Rights Reserved.
# Author: ZhangT
# Author-Github: github.com/zhangt2333
# spider.py 2018/7/8 19:41

import requests
from requests.exceptions import RequestException
import config
import re
import json
import time

def set_Cookies():
    """访问教务系统得到的requests中headers头的cookie，并记录在config文件的变量中，返回执行真值"""
    url = 'http://bkjwxk.sdu.edu.cn/f/common/main'
    try:
        response = requests.get(url)
        if response.status_code == 200:
            cookiejar = response.request._cookies
            # 上句中cookiesjar形如:
            # <RequestsCookieJar[<Cookie JSESSIONID=略 for bkjwxk.sdu.edu.cn/>, <Cookie sduxk=略 for bkjwxk.sdu.edu.cn/>]>
            # 转换成字典如下保存起来即可
            cookies = requests.utils.dict_from_cookiejar(cookiejar)
            config.Cookies['JSESSIONID'] = cookies['JSESSIONID']
            config.Cookies['sduxk'] = cookies['sduxk']
            return True
        else:
            return False
    except RequestException:
        return False


def login(j_username, j_password):
    """登陆学号，返回登陆结果，真则存入cookie到HEADER。前提：已配置Cookies成功"""
    url = 'http://bkjwxk.sdu.edu.cn/b/ajaxLogin'
    # config.Cookies['j_username'] = j_username
    # config.Cookies['j_password'] = j_password
    data = {}
    data['j_username'] = j_username
    data['j_password'] = config.generateMD5(j_password)
    try:
        response = requests.post(url, headers=config.HEADERS, cookies=config.Cookies, data=data)
        text = response.text
        if response.status_code == 200 and 'success' in text:
            return True
        return False
    except RequestException:
        return False


def get_SelectedCourses():
    """得到、用RE解析已选课的列表。前提：已登陆成功"""
    url = 'http://bkjwxk.sdu.edu.cn/f/xk/xs/yxkc'
    re1 = 'color.*?>(.*?)</font>'  # 拿已选课的学分信息
    re2 = '<td>(.*?)</td>'  # 拿已选课的表项
    Course_info = ''
    Courses = []
    try:
        response = requests.post(url, headers=config.HEADERS, cookies=config.Cookies)
        if response.status_code == 200:
            text = response.text
            Course_info = re.findall(re.compile(re1, re.S), text)[0]
            items = re.findall(re.compile(re2, re.S), text)
            for index in range(0, len(items), 9):  # 以9为步长，遍历、处理结果
                item = []
                for i in range(9):  # 表头: 课程号 课程名称 课序号 学分 上课时间 任课教师 课程属性 开课学院 选课结果
                    item.append(items[index + i])
                Courses.append(item)
        return {'Course_info': Course_info, 'Courses': Courses}
    except RequestException:
        return None


def query_Course(kch, kxh):
    """以课程号、课序号查询某课程的信息，如课余量。前提：已登录成功"""
    url = 'http://bkjwxk.sdu.edu.cn/b/xk/xs/kcsearch'
    data = {"type": "kc",
            "currentPage": "1",
            "kch": str(kch),
            "jsh": "",
            "skxq": "",
            "skjc": "",
            "kkxsh": ""}
    try:
        response = requests.post(url, headers=config.HEADERS, cookies=config.Cookies, data=data)
        text = response.text
        if response.status_code == 200 and 'success' in text:
            items = json.loads(text)['object']['resultList']
            # 校验课序号并返回
            for item in items:
                if item['KXH'] == str(kxh):
                    return item
        return None
    except RequestException:
        return None


def add_Course(kch, kxh):
    """以课程号、课序号为依据，将该门课添入选课栏。前提：已登录成功"""
    time.sleep(1.9)  # 选课退课的限制，可以自己取消
    url = 'http://bkjwxk.sdu.edu.cn/b/xk/xs/add/' + str(kch) + '/' + str(kxh)
    try:
        response = requests.post(url, headers=config.HEADERS, cookies=config.Cookies)
        text = response.text
        if response.status_code == 200:
            return json.loads(text)['msg']
        return None
    except RequestException:
        return False


def delete_Course(kch, kxh):
    """以课程号、课序号为依据，将该门课从选课栏退去。前提：已登录成功"""
    time.sleep(1.9)  # 选课退课的限制，可以自己取消
    url = 'http://bkjwxk.sdu.edu.cn/b/xk/xs/delete'
    data = {'aoData': '',
            'kchkxh': str(kch) + '|' + str(kxh)}
    try:
        response = requests.post(url, headers=config.HEADERS, cookies=config.Cookies, data=data)
        text = response.text
        if response.status_code == 200:
            return json.loads(text)['msg']
        return None
    except RequestException:
        return None


def draw_Course(kch, kxh):
    """以课程号、课序号为依据，将某门课抽签。前提：已登录成功"""
    time.sleep(1.9)  # 选课退课的限制，可以自己取消
    url = 'http://bkjwxk.sdu.edu.cn/b/xk/xs/cq/' + str(kch) + '/' + str(kxh)
    try:
        response = requests.post(url, headers=config.HEADERS, cookies=config.Cookies)
        text = response.text
        if response.status_code == 200:
            return json.loads(text)['msg']
        return None
    except RequestException:
        return False
