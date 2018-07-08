# -*- coding: utf-8 -*-
#!/usr/bin/env python
# Copyright 2018 ZhangT. All Rights Reserved.
# Author: ZhangT
# Author-Github: github.com/zhangt2333
# main_demo.py 2018/7/8 22:22

import spider

prompt_words = '您现在测试的是【SDU选课助手api】的命令行demo，功能如下：' + '\n' + \
               '0.配置cookies (登录前必须做) 命令格式(引号内)："0" ' + '\n' +\
               '1.登录账号 命令格式(引号内)："1 你的学号 教务密码" ' + '\n' +\
               '2.查询已选课 (前提：已登录成功) 命令格式(引号内)："2" ' + '\n' +\
               '3.查询某一门课情况 (前提：已登录成功) 命令格式(引号内) ："3 课程号 课序号"' + '\n' +\
               '4.选某一门课 (前提：已登录成功) 命令格式(引号内) ："4 课程号 课序号"' + '\n' +\
               '5.退某一门课 (前提：已登录成功) 命令格式(引号内) ："5 课程号 课序号"' + '\n' +\
               '6.抽签某一门课 (前提：已登录成功) 命令格式(引号内) ："6 课程号 课序号"' + '\n' +\
               '7.退出程序 命令格式(引号内) ："7" ' + '\n' +\
               '请输入操作:'


def deal_with_command(str):
    """处理命令"""
    if str[0] == '0':
        print(spider.set_Cookies())
    elif str[0] == '1':
        print(spider.login(str[1], str[2]))
    elif str[0] == '2':
        print(spider.get_SelectedCourses())
    elif str[0] == '3':
        print(spider.query_Course(str[1], str[2]))
    elif str[0] == '4':
        print(spider.add_Course(str[1], str[2]))
    elif str[0] == '5':
        print(spider.delete_Course(str[1], str[2]))
    elif str[0] == '6':
        print(spider.draw_Course(str[1], str[2]))


if __name__ == '__main__':
    while True:
        str = [x for x in input(prompt_words).split()]
        if str[0] == '7':
            exit(0)
        deal_with_command(str)
