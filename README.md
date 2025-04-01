# Awesome-SDU-Script

与 SDU 日常相关的一些爬虫/脚本，如绩点查询器、选课助手、图书馆预约助手、教评助手、青岛校区电量查询、校园网认证脚本、实验报告 LaTeX 模板等，欢迎研究和使用:smile:

Some scripts about the life at SDU, like GPA-Spider, Selecting-Courses-Assistant, and so on. Welcome! :smile:


# 目录

* [目录](#目录)
* [Latest](#latest)
   * [图书馆座位预约脚本 sdu-lib-seat](#图书馆座位预约脚本-sdu-lib-seat)
   * [选课脚本 sduContentionCourse](#选课脚本-sducontentioncourse)
   * [青岛校区电量查询器 SDU-QD-Electricity-Query-Script](#青岛校区电量查询器-SDU-QD-Electricity-Query-Script)
   * [青岛校区校园网认证 sdunetd](#青岛校区校园网认证-sdunetd)
   * [实验报告 LaTex 模板 sdu_report_song](#实验报告-latex-模板-sdu_report_song)
   * [实验报告 Typst 模板 sdu-exp-report](#实验报告-typst-模板-sdu-exp-report)
   
* [Archived](#archived)
   * [绩点查询器 GPA-Spider](#绩点查询器-gpa-spider)
   * [绩点查询器(GUI) GPA-Spider-GUI](#绩点查询器gui-gpa-spider-gui)
   * [选课助手 Selecting-Courses-Assistant](#选课助手-selecting-courses-assistant)
   * [教评助手 Teaching-Evaluation-Assistant](#教评助手-teaching-evaluation-assistant)
   * [青岛校区电量查询器 Electricity-Spider](#青岛校区电量查询器-electricity-spider)
   * [青岛校区电量查询器 (golang) sdu-qd-electricity-bill](#青岛校区电量查询器-golang-sdu-qd-electricity-bill)
   * [青岛校区宿舍低电自动提醒 actions-SduElectricityReminder](#青岛校区宿舍低电自动提醒-actions-sduelectricityreminder)
* [Contribution](#contribution)
* [License](#license)

# Latest

## 图书馆座位预约脚本 `sdu-lib-seat`

- 山东大学各校区图书馆座位预约
- Docker部署/集成crontab-ui图形界面/提供测试环境/支持自动化定时预约

## 选课脚本 `sduContentionCourse`

* SDU 选课脚本
* 开箱即用，基于浏览器直接运行，不需要下载脚本或其他文件

## 青岛校区电量查询器 `SDU-QD-Electricity-Query-Script`
* 还在为山大V卡通 2.0 更新后原脚本失效而苦恼？
* 一键解决原脚本失效问题！



## 青岛校区校园网认证 `sdunetd`

* 供无图形化界面的 Linux 系统进行校园网认证

## 实验报告 LaTex 模板 `sdu_report_song`

* LaTeX 模板用于实验报告(*~~song的意思为宋体~~*)
![sdu_report_song](https://github.com/Naylenv/sdu_report_song/raw/master/figures/demo.png)

## 实验报告 Typst 模板 `sdu-exp-report`

* Typst 模板用于实验报告，使用更简单的语法，更快的速度，获取更好的效果。
![sdu-exp-report](https://github.com/Dregen-Yor/sdu-exp-report/blob/main/example/figures/main.png)

# Archived

## 青岛校区电量查询器 `Electricity-Spider`

<details>
<summary>山大V卡通2.0更新后，原API被废弃，该脚本 archived!，点击查看旧描述</summary>

  * 夜晚开黑，停电，充电后来电已是明早！ 突然停电，台式机数据丢失！
  * 青岛校区电量查询，将以上情形一网打尽！
  * 山大V卡通2.0更新后，原API被废弃

</details>


## 青岛校区电量查询器 (golang) `sdu-qd-electricity-bill`

<details>
<summary>山大V卡通2.0更新后，原API被废弃，该脚本 archived!，点击查看旧描述</summary>

  * 青岛校区电量查询器，Go 语言编写！！

</details>

## 青岛校区宿舍低电自动提醒 `actions-SduElectricityReminder`

<details>
<summary>山大V卡通2.0更新后，原API被废弃，该脚本 archived!，点击查看旧描述</summary>

  * 自动查 [SDU 青岛校区] 宿舍电量，低于阈值则邮件提醒
  * 不需要自己购买服务器，也不需要自己配置服务器，真的 Serverless !!

</details>



## 绩点查询器 `GPA-Spider`

<details>
<summary>由于教务系统被升级替换，该脚本 archived!，点击查看描述</summary>

  * [Download the binary for Windows-64]( https://github.com/zhangt2333/SDU-Funny-Scripts/releases/download/v1.0/GPA_spider.exe) 
  * 查询 SDU 学生学期成绩，并根据输入的学年学期进行加权绩点的计算
  * 简易、核心、实现基本功能，使用体验较差
    ![](GPA-Spider/pic1.png)

</details>

## 绩点查询器(GUI) `GPA-Spider-GUI`

<details>
<summary>由于教务系统被升级替换，该脚本 archived!，点击查看描述</summary>

  * 查询 SDU 学生学期成绩，并根据输入的学年学期进行加权绩点的计算
  * 使用体验一般，但实现了 GUI，学习了一波 pyqt5
    ![](GPA-Spider-GUI/pic1.jpg)

</details>

## 选课助手 `Selecting-Courses-Assistant`

<details>
<summary>由于教务系统被升级替换，该脚本 archived!，点击查看描述</summary>

  * 规范的教务选课系统 API，代码有详细的注释
  * ~~少量的改动 (增加具体的课程号和循环)，可以进化成 `抢课助手`~~
  * 为了校园和平，没有 GUI 版，有能力改动她的人理应要有相应的价值观
    附上 demo：
    ![](Selecting-Courses-Assistant/pic1.png)

</details>

## 教评助手 `Teaching-Evaluation-Assistant`

<details>
<summary>由于教务系统被升级替换，该脚本 archived!，点击查看旧描述</summary>

  * 解决期末查成绩前的拦路虎 —— 反人类的教评提交交互！
  * 实现所有课程一键全部满分好评（需要特殊打分去教务系统教评一次即可）
    ![](Teaching-Evaluation-Assistant/pic1.png)

</details>

# Contribution

本仓库旨在收集使得 SDU 生活更美好的一些脚本，如果有意被收录到本仓库，请提交 Issue 或 PR 参与贡献！

Looking forward to your contribution!

# License

MIT：`被授权人有权利在软件和软件的所有副本中包含版权声明和许可声明的前提下，使用、复制、修改、合并、出版发行、散布、再授权及贩售软件及软件的副本。授权人不为被授权人行为承担任何责任，且无义务对著作进行更新。`
