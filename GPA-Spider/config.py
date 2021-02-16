# -*- coding: utf-8 -*-
#!/usr/bin/env python
# Copyright 2018 ZhangT. All Rights Reserved.
# Author: ZhangT
# Author-Github: github.com/zhangt2333
# config.py 2018/2/10 21:49

# 包含一些通用常量和工具函数

HEADERS = {"Host": "bkjws.sdu.edu.cn",
           "Connection": "keep-alive",
           "Accept": "*/*",
           "Origin": "http://bkjws.sdu.edu.cn",
           "X-Requested-With": "XMLHttpRequest",
           "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
           "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
           "Accept-Language": "zh-CN,zh;q=0.8"}

# 获取成绩时候的post数据
aoData = 'aoData=%5B%7B%22name%22%3A%22sEcho%22%2C%22value%22%3A1%7D%2C%7B%22' \
    'name%22%3A%22iColumns%22%2C%22value%22%3A8%7D%2C%7B%22name%22%3A%22' \
    'sColumns%22%2C%22value%22%3A%22%22%7D%2C%7B%22name%22%3A%22iDisplay' \
    'Start%22%2C%22value%22%3A0%7D%2C%7B%22name%22%3A%22iDisplayLength%2' \
    '2%2C%22value%22%3A-1%7D%2C%7B%22name%22%3A%22mDataProp_0%22%2C%22va' \
    'lue%22%3A%22function%22%7D%2C%7B%22name%22%3A%22mDataProp_1%22%2C%2' \
    '2value%22%3A%22kch%22%7D%2C%7B%22name%22%3A%22mDataProp_2%22%2C%22v' \
    'alue%22%3A%22kcm%22%7D%2C%7B%22name%22%3A%22mDataProp_3%22%2C%22val' \
    'ue%22%3A%22kxh%22%7D%2C%7B%22name%22%3A%22mDataProp_4%22%2C%22value' \
    '%22%3A%22xf%22%7D%2C%7B%22name%22%3A%22mDataProp_5%22%2C%22value%22' \
    '%3A%22kssj%22%7D%2C%7B%22name%22%3A%22mDataProp_6%22%2C%22value%22%' \
    '3A%22kscjView%22%7D%2C%7B%22name%22%3A%22mDataProp_7%22%2C%22value%' \
    '22%3A%22kcsx%22%7D%2C%7B%22name%22%3A%22iSortingCols%22%2C%22value%' \
    '22%3A0%7D%2C%7B%22name%22%3A%22bSortable_0%22%2C%22value%22%3Afalse' \
    '%7D%2C%7B%22name%22%3A%22bSortable_1%22%2C%22value%22%3Afalse%7D%2C' \
    '%7B%22name%22%3A%22bSortable_2%22%2C%22value%22%3Afalse%7D%2C%7B%22' \
    'name%22%3A%22bSortable_3%22%2C%22value%22%3Afalse%7D%2C%7B%22name%2' \
    '2%3A%22bSortable_4%22%2C%22value%22%3Afalse%7D%2C%7B%22name%22%3A%22' \
    'bSortable_5%22%2C%22value%22%3Afalse%7D%2C%7B%22name%22%3A%22bSortab' \
    'le_6%22%2C%22value%22%3Afalse%7D%2C%7B%22name%22%3A%22bSortable_7%22' \
    '%2C%22value%22%3Afalse%7D%5D'


def strB2Q(ustring):
    """工具函数：全角转半角"""
    rstring = ""
    for uchar in ustring:
        inside_code = ord(uchar)
        if inside_code == 32:  # 全角空格直接转换
            inside_code = 12288
        elif (inside_code >= 33 and inside_code <= 126):  # 全角字符（除空格）根据关系转化
            inside_code += 65248
        rstring += chr(inside_code)
    return rstring


def Align_CHstr(str, format_spec):
    """工具函数：处理一个中英文混杂str的填充对齐"""
    format_spec = "{0:{1}" + format_spec + "}"
    return format_spec.format(strB2Q(str), chr(12288))

def compare_xnxq(xnxq1, xnxq2):
    """返回 xnxq1 > xnxq2"""
    tmp = xnxq1.split('-')
    xnxq1 = tmp[2] + tmp[1]*10 + tmp[0]*10000
    tmp = xnxq2.split('-')
    xnxq2 = tmp[2] + tmp[1]*10 + tmp[0]*10000
    return xnxq1 > xnxq2