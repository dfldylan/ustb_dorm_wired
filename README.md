# ustb_dorm_wired
北京科技大学宿舍有线网口打开脚本

2019年学校对宿舍网络进行了改造，每个宿舍增加了USTB-Student的ap发射点，但是屏蔽了ap的有线网口，该串口脚本可以打开有线网口。

# 运行环境
Windows 10

# router.py
主脚本
# router.bat
守护脚本

# 用法
首先需要买一根路由器console线，将路由器console口连接电脑，在电脑上操作

运行router.py即可

建议把router.bat挂到系统启动项，该守护脚本每十分钟运行一次router.bat

详细教程：
https://evanzj.com/2021/11/29/H3B2/
