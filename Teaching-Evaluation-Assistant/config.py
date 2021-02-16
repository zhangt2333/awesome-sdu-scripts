# -*- coding: utf-8 -*-
#!/usr/bin/env python
# Copyright 2018 ZhangT. All Rights Reserved.
# Author: ZhangT
# Author-Github: github.com/zhangt2333
# config.py 2018/2/10 21:49

# 包含一些通用常量和工具函数

import hashlib

HEADERS = {"Host": "bkjws.sdu.edu.cn",
           "Connection": "keep-alive",
           "Accept": "*/*",
           "Origin": "http://bkjws.sdu.edu.cn",
           "X-Requested-With": "XMLHttpRequest",
           "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
           "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
           "Accept-Language": "zh-CN,zh;q=0.8"}

EVALUATION_LIST_DATA = 'aoData=%5B%7B%22name%22%3A%22sEcho%22%2C%22value%22%3A1%7D%2C%7B%22name%22%3A%22iColumns%22%2C%22value%22%3A5%7D%2C%7B%22name%22%3A%22sColumns%22%2C%22value%22%3A%22%22%7D%2C%7B%22name%22%3A%22iDisplayStart%22%2C%22value%22%3A0%7D%2C%7B%22name%22%3A%22iDisplayLength%22%2C%22value%22%3A-1%7D%2C%7B%22name%22%3A%22mDataProp_0%22%2C%22value%22%3A%22kch%22%7D%2C%7B%22name%22%3A%22mDataProp_1%22%2C%22value%22%3A%22kcm%22%7D%2C%7B%22name%22%3A%22mDataProp_2%22%2C%22value%22%3A%22jsm%22%7D%2C%7B%22name%22%3A%22mDataProp_3%22%2C%22value%22%3A%22function%22%7D%2C%7B%22name%22%3A%22mDataProp_4%22%2C%22value%22%3A%22function%22%7D%2C%7B%22name%22%3A%22iSortCol_0%22%2C%22value%22%3A0%7D%2C%7B%22name%22%3A%22sSortDir_0%22%2C%22value%22%3A%22asc%22%7D%2C%7B%22name%22%3A%22iSortingCols%22%2C%22value%22%3A1%7D%2C%7B%22name%22%3A%22bSortable_0%22%2C%22value%22%3Atrue%7D%2C%7B%22name%22%3A%22bSortable_1%22%2C%22value%22%3Afalse%7D%2C%7B%22name%22%3A%22bSortable_2%22%2C%22value%22%3Afalse%7D%2C%7B%22name%22%3A%22bSortable_3%22%2C%22value%22%3Afalse%7D%2C%7B%22name%22%3A%22bSortable_4%22%2C%22value%22%3Afalse%7D%5D'

DEFALUT_EVALUATION_PARM = 'wjid=1&wjmc=%E5%B1%B1%E4%B8%9C%E5%A4%A7%E5%AD%A6%E8%AF%BE%E5%A0%82%E6%95%99%E5%AD%A6%E8%AF%84%E4%BB%B7(2017)&zbid=36&zblx=%E9%80%89%E6%8B%A9&sfbt=&zbda_0=5.0&zbid=37&zblx=%E9%80%89%E6%8B%A9&sfbt=&zbda_1=5.0&zbid=38&zblx=%E9%80%89%E6%8B%A9&sfbt=&zbda_2=5.0&zbid=39&zblx=%E9%80%89%E6%8B%A9&sfbt=&zbda_3=5.0&zbid=40&zblx=%E9%80%89%E6%8B%A9&sfbt=&zbda_4=5.0&zbid=41&zblx=%E9%80%89%E6%8B%A9&sfbt=&zbda_5=5.0&zbid=42&zblx=%E9%80%89%E6%8B%A9&sfbt=&zbda_6=5.0&zbid=43&zblx=%E9%80%89%E6%8B%A9&sfbt=&zbda_7=5.0&zbid=44&zblx=%E9%80%89%E6%8B%A9&sfbt=&zbda_8=5.0&zbid=45&zblx=%E9%80%89%E6%8B%A9&sfbt=&zbda_9=5.0&zbid=46&zblx=%E9%80%89%E6%8B%A9&sfbt=&zbda_10=5.0&zbid=47&zblx=%E9%80%89%E6%8B%A9&sfbt=&zbda_11=5.0&zbid=48&zblx=%E9%80%89%E6%8B%A9&sfbt=&zbda_12=5.0&zbid=49&zblx=%E9%80%89%E6%8B%A9&sfbt=&zbda_13=5.0&zbid=50&zblx=%E9%80%89%E6%8B%A9&sfbt=&zbda_14=5.0&zbid=52&zblx=%E9%80%89%E6%8B%A9&sfbt=&zbda_15=5.0&zbid=53&zblx=%E9%80%89%E6%8B%A9&sfbt=&zbda_16=5.0&zbid=54&zblx=%E9%80%89%E6%8B%A9&sfbt=&zbda_17=5.0&zbid=55&zblx=%E9%80%89%E6%8B%A9&sfbt=&zbda_18=10.0&zbid=51&zblx=%E4%B8%BB%E8%A7%82%E9%80%89%E6%8B%A9&sfbt=&zbda_19=%E8%AF%BE%E7%A8%8B%E6%9C%89%E6%8C%91%E6%88%98%E6%80%A7&zbid=56&zblx=%E4%B8%BB%E8%A7%82%E9%80%89%E6%8B%A9&sfbt=&zbda_20=%E4%B8%8D%E6%8E%A8%E8%8D%90&zbid=57&zblx=%E4%B8%BB%E8%A7%82&sfbt=%E6%98%AF&zbda_21=%E8%B5%9E%EF%BC%81'

def generateMD5(str):
    """工具函数：md5编码"""
    hl = hashlib.md5()
    hl.update(str.encode(encoding='utf-8'))
    return hl.hexdigest()


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

