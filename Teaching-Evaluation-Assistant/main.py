# -*- coding: utf-8 -*-
#!/usr/bin/env python
# Copyright 2018 ZhangT. All Rights Reserved.
# Author: ZhangT
# Author-Github: github.com/zhangt2333
# main.py 2019/1/18 10:24

from spider import *

def main():
    username = input('请输入学号: ')
    password = input('请输入密码: ')
    print('下面将为你进行所有课的教评，一律好评，如需特殊打分，请自行到教务系统教评即可，最新的记录会覆盖上次的教评记录')
    print(login(username, password))
    evaluation_list = get_evaluation_list()
    print(evaluation_list)
    for i in evaluation_list:
        print(i, default_evaluate_one_course(i['xnxq'], i['kch'], i['jsh']))


if __name__ == "__main__":
    main()
