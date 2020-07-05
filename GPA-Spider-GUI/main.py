# -*- coding: utf-8 -*-
#!/usr/bin/env python
# Copyright 2018 ZhangT. All Rights Reserved.
# Author: ZhangT
# Author-Github: github.com/zhangt2333
# main.py 2018/2/26 21:37

import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QLineEdit, QInputDialog

from UI import *
import GPA_spider


class mywindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_tablescores()
        self.flag_logined = False

    def login(self):
        self.Button_login.setEnabled(False)
        if not GPA_spider.set_Cookie():
            QMessageBox.critical(self, "程序提醒您：", "配置cookie失败！！\n请重新检查网络后启动.\n若确认为程序问题请向作者报告此bug")
            return

        response_login = GPA_spider.login(self.input_id.text(), self.input_passwd.text())
        if '输入有误' in response_login:
            QMessageBox.critical(self, "程序提醒您：", "对不起,用户名或密码输入有误,请重新输入!")
            self.input_passwd.setText("")
            return
        elif 'success' not in response_login:
            QMessageBox.critical(self, "程序提醒您：", "对不起，登录失败，请重新登录")
            self.input_passwd.setText("")
            return

        # 获得姓名
        profile = GPA_spider.get_profile()
        self.label_nowuser.setText("当前用户：" + profile['姓名'] + " | 学院：" + profile['学院'] +
                                   " | 专业：" + profile['专业名'] + " | 班级:" + profile['班名'])
        self.init_tablescores()
        self.flag_logined = True
        QMessageBox.information(self, "程序提醒您：", "用户：" + profile['姓名'] + "\n登录成功！！")
        self.Button_login.setEnabled(True)
        self.Button_getscores.setEnabled(True)

    def getscores(self):
        self.Button_getscores.setEnabled(False)
        if not self.flag_logined:
            QMessageBox.information(self, "程序提醒您：", "请先登录！")
            return
        self.scores = GPA_spider.get_scores()
        index = 0
        for score in self.scores:
            self.model.setItem(index, 0, QtGui.QStandardItem(score["学年学期"]))
            self.model.setItem(index, 1, QtGui.QStandardItem(score["课程名"]))
            self.model.setItem(index, 2, QtGui.QStandardItem(score["课程属性"]))
            self.model.setItem(index, 3, QtGui.QStandardItem(str(score["学分"])))
            self.model.setItem(index, 4, QtGui.QStandardItem(score["最终成绩"]))
            self.model.setItem(index, 5, QtGui.QStandardItem(score["评分"]))
            self.model.setItem(index, 6, QtGui.QStandardItem(score["绩点"]))
            self.model.setItem(index, 7, QtGui.QStandardItem(str(score["期末成绩"])))
            self.model.setItem(index, 8, QtGui.QStandardItem(str(score["平时成绩"])))
            index += 1
        self.Button_getscores.setEnabled(True)
        self.Button_calGPA.setEnabled(True)

    def calGPA(self):
        self.Button_calGPA.setEnabled(False)
        xnxq = self.model.data(self.model.index(0, 0))
        if xnxq:
            str, OKevent = QInputDialog.getText(self, "程序提醒您：", "请输入要计算绩点的学年学期（完全匹配）：:", QLineEdit.Normal, xnxq)
            if OKevent and str.strip():
                self.label_GPA.setText(str.strip() + "_GPA：" + GPA_spider.cal_GPA(self.scores, str.strip()))
        self.Button_calGPA.setEnabled(True)

    def init_tablescores(self):

        self.model = QtGui.QStandardItemModel(self.table_scores)
        self.model.setHorizontalHeaderItem(0, QtGui.QStandardItem("学年学期"))
        self.model.setHorizontalHeaderItem(1, QtGui.QStandardItem("课程名"))
        self.model.setHorizontalHeaderItem(2, QtGui.QStandardItem("属性"))
        self.model.setHorizontalHeaderItem(3, QtGui.QStandardItem("学分"))
        self.model.setHorizontalHeaderItem(4, QtGui.QStandardItem("最终成绩"))
        self.model.setHorizontalHeaderItem(5, QtGui.QStandardItem("评分"))
        self.model.setHorizontalHeaderItem(6, QtGui.QStandardItem("绩点"))
        self.model.setHorizontalHeaderItem(7, QtGui.QStandardItem("期末成绩"))
        self.model.setHorizontalHeaderItem(8, QtGui.QStandardItem("平时成绩"))
        self.table_scores.setModel(self.model)
        self.table_scores.setColumnWidth(0, 80)
        self.table_scores.setColumnWidth(1, 150)
        self.table_scores.setColumnWidth(2, 37)
        self.table_scores.setColumnWidth(3, 30)
        self.table_scores.setColumnWidth(4, 55)
        self.table_scores.setColumnWidth(5, 30)
        self.table_scores.setColumnWidth(6, 30)
        self.table_scores.setColumnWidth(7, 55)
        self.table_scores.setColumnWidth(8, 55)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = mywindow()
    mainWindow.show()
    sys.exit(app.exec_())
