## wechat-jump-game

# 玩微信跳一跳游戏的脚本

用到的库和软件

* android adb
* Python27
* Python PIL库
* python Tkinter, os, sys, time

使用方法


1. connect android with usb

2. adb connect

3. open jump game and start

4. 点击pull按钮，进入点击起始点的状态（select point one）

5. 鼠标右点击起始点，进入结束点的选择状态（select point two）

6. 鼠标右击结束点，结束一次跳转动计算（选择完结束点后程序自动给手机发送跳动命令）

7. 等待一秒钟后从第五个步骤开始重复（主要是看log，第一个节点第二个节点按顺序重复选择即可， 如果顺序乱了也可以从第四个步骤开始重复）

效果图

![demo](demo.png)
