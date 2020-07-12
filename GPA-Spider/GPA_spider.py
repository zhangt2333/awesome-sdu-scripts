# -*- coding: utf-8 -*-
#!/usr/bin/env python
# Copyright 2018 ZhangT. All Rights Reserved.
# Author: ZhangT
# Author-Github: github.com/zhangt2333
# GPA-Spider.py 2018/2/10 20:31
import json
import os
from config import generateMD5
import config
import requests
from requests.exceptions import RequestException
import sys


def set_Cookie():
    """统一程序中发送requests请求的所有cookie，即加到headers里面"""
    try:
        response = requests.get('http://bkjwxk.sdu.edu.cn/f/common/main')
        if response.status_code == 200:
            config.JSESSIONID = response.request._cookies._cookies
            config.JSESSIONID = str(config.JSESSIONID['bkjwxk.sdu.edu.cn']['/']['JSESSIONID'])[19:40]
            config.HEADERS["Cookie"] = "JSESSIONID=" + config.JSESSIONID
            return True
        else:
            return False
    except RequestException:
        return False


def login(username, password):
    """登录，返回一个response"""
    data = "j_username=" + username + "&j_password=" + generateMD5(password)
    try:
        response = requests.post('http://bkjws.sdu.edu.cn/b/ajaxLogin', data=data, headers=config.HEADERS)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None


def get_profile():
    """获得使用者姓名"""
    try:
        response = requests.post('http://bkjws.sdu.edu.cn/b/grxx/xs/xjxx/detail', headers=config.HEADERS)
        if response.status_code == 200 and '"success"' in response.text:
            profile_json = json.loads(response.text)["object"]
            return {
                "姓名": profile_json["xm"],
                "学院": profile_json['xsm'],
                "专业名": profile_json['zym'],
                "班名": profile_json["bm"],
                "入学日期": profile_json['rxrq']
            }
        else:
            return None
    except RequestException:
        return None


def get_now_score():
    """返回一个本学期成绩json"""
    try:
        response = requests.post('http://bkjws.sdu.edu.cn/b/cj/cjcx/xs/list', data=config.aoData,
                                 headers=config.HEADERS)
        if response.status_code == 200 and 'success' in response.text:
            return json.loads(response.text)
        return None
    except RequestException:
        return None


def get_past_score():
    """返回一个所谓历年成绩json"""
    try:
        response = requests.post('http://bkjws.sdu.edu.cn/b/cj/cjcx/xs/lscx', data=config.aoData,
                                 headers=config.HEADERS)
        if response.status_code == 200 and 'success' in response.text:
            return json.loads(response.text)
        return None
    except RequestException:
        return None


def parse_json(score_json):
    """解析成绩json，迭代每一科成绩，yield一个长str"""
    sub_aaData = score_json['object']['aaData']
    for item in sub_aaData:
        yield {
            "学年学期": item['xnxq'] if 'xnxq' in item else '空',
            "课程名": item['kcm'],
            # "教师名": item['jsm'],
            "课程属性": item['kcsx'],
            "学分": item['xf'],
            "最终成绩": item['kscjView'],
            "评分": item['wfzdj'],
            "绩点": item['wfzjd'],
             # "期末成绩": item['qmcj'],
            # "平时成绩": item['pscj'],
        }


def get_scores():
    score_now_json = get_now_score()
    score_past_json = get_past_score()
    scores = []
    for score in parse_json(score_now_json):
        scores.append(score)
    for score in parse_json(score_past_json):
        scores.append(score)
    max_xnxq = None
    for score in scores:
        if score['学年学期'] != '空' and (not max_xnxq or config.compare_xnxq(score['学年学期'], max_xnxq)):
            max_xnxq = score['学年学期']
    for score in scores:
        if score['学年学期'] == '空':
            score['学年学期'] = max_xnxq
    scores.sort(key=lambda x: x['学分'], reverse=True)
    return scores


def Align(string, length=0):
    if length == 0:
        return string
    slen = len(string)
    re = string
    if isinstance(string, str):
        placeholder = ' '
    else:
        placeholder = u'　'
    while slen < length:
        re += placeholder
        slen += 1
    return re


def show_scores(scores):
    """格式化输出成绩"""
    # 获得课程名最大长度
    maxLen = 0
    for score in scores:
        if len(score["课程名"]) > maxLen:
            maxLen = len(score["课程名"])
    # 输出表头
    print("| 学年学期  |" + config.Align_CHstr("课程名", "^" + str(maxLen)) + "|课程属性|" + "学分|" +
          "最终成绩|" + "评分|" + "绩点|" + "期末成绩|" + "平时成绩|")
    # 输出表单
    for score in scores:
        print(format(score["学年学期"], "<13") + config.Align_CHstr(score["课程名"], "<" + str(maxLen)) + " " +
              format(score["课程属性"], "^4") + " " + format(score["学分"], "<3") + "   " +
              format(str(score["最终成绩"]), "<3") + "   " + format(str(score["评分"]), "<2") + "  " +
              format(str(score["绩点"]), "^4")) # + "  " + format(str(score["期末成绩"]), "^5") + " " +
             # format(str(score["平时成绩"]), "^7"))


def cal_GPA(scores, xnxq):
    """计算绩点"""
    GPA = 0.0
    sum_credits = 0.0
    for score in scores:
        if (score["学年学期"] == xnxq or xnxq == 'all') and score['课程属性'] in ['必修', '限选']:
            print(score)
            sum_credits += float(score["学分"])
            GPA += float(score["学分"]) * float(score["绩点"])
    if sum_credits != 0:
        return GPA / sum_credits
    else:
        return 0.0


def main():
    print("--------欢迎您使用GPA_spider!!!--------")
    # 配置cookie
    if set_Cookie():
        print("配置cookie成功")
    else:
        print("配置cookie失败！！请重新检查网络后启动，若确认为程序问题请向作者报告此bug")
        sys.exit()
    # 输入
    id = input("请输入SDU学号：")
    passwd = input("请输入选课密码：")
    # 登录
    print("正在登录...")
    response_login = login(id, passwd)
    if '"success"' in response_login:
        print("登录成功!")
    elif '输入有误' in response_login:
        print(response_login)
        sys.exit()
    else:
        print("其他登录失败原因！！请重新检查网络后启动，若确认为程序问题请向作者报告此bug")
        sys.exit()
    # 获得姓名
    profile = get_profile()
    print("使用者：" + profile['姓名'] + "|学院：" + profile['学院'] +
          "|专业：" + profile['专业名'] + "|班级:" + profile['班名'])
    # 获取成绩
    print("正在获取本学年成绩...")
    scores = get_scores()
    show_scores(scores)
    # 计算绩点
    xnxq = input("您现在可以选择输入需要计算绩点的学年学期（完全匹配，计算全部则输入'all'）：")
    GPA = cal_GPA(scores, xnxq)
    print(GPA)


if __name__ == "__main__":
    main()
