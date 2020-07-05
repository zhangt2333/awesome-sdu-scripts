# SDU-Funny-Scripts
与 SDU 日常相关的一些爬虫/脚本，如绩点查询器、抢课助手等，欢迎研究和使用:smile:

Some spiders/scripts about the life in SDU, like GPA-Spider, Selecting-Courses-Assistant, and so on. Weclome !​ :smile:



TODO:

-   [ ] 接入统一登录
-   [ ] ... 其他好玩的 spider 开发



# 目录

*   绩点查询器
*   绩点查询器 (GUI)
*   选课助手
*   教评助手



# 1  绩点查询器 `GPA-Spider`

*   [Download the binary for Windows-64]( https://github.com/zhangt2333/SDU-Funny-Scripts/releases/download/v1.0/GPA_spider.exe) 
*   查询 SDU 学生学期成绩，并根据输入的学年学期进行加权绩点的计算
*   简易、核心、实现基本功能，使用体验较差

![](GPA-Spider/pic1.png)

# 2  绩点查询器(GUI) `GPA-Spider-GUI`

*   查询 SDU 学生学期成绩，并根据输入的学年学期进行加权绩点的计算
*   使用体验一般，但实现了 GUI，学习了一波 pyqt5

![](GPA-Spider-GUI/pic1.jpg)

# 3  选课助手 `Selecting-Courses-Assistant`

*   规范的教务选课系统 API，代码有详细的注释
*   ~~少量的改动 (增加具体的课程号和循环)，可以进化成 `抢课助手`~~
*   为了校园和平，没有 GUI 版，有能力改动她的人理应要有相应的价值观

附上 demo：

![](Selecting-Courses-Assistant/pic1.png)



# 4  教评助手 `Teaching-Evaluation-Assistant`

解决期末查成绩前的拦路虎 —— 反人类的教评提交交互！

*   实现所有课程一键全部满分好评（需要特殊打分去教务系统教评一次即可）

![](Teaching-Evaluation-Assistant/pic1.png)



# License

MIT：`被授权人有权利在软件和软件的所有副本中包含版权声明和许可声明的前提下，使用、复制、修改、合并、出版发行、散布、再授权及贩售软件及软件的副本。授权人不为被授权人行为承担任何责任，且无义务对著作进行更新。`