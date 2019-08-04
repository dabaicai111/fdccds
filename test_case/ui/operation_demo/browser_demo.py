#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'dabaicai'
__mtime__ = '2019/7/30'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☆    ┃
            ┃  ┳┛  ┗┳ ┃
            ┃      ┻    ┃
            ┗━┓     ┏━┛
                ┃     ┗━━━┓
                ┃ 大白菜保佑   ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""
# 打开
from time import sleep

from selenium import webdriver

from config.conf import DRIVER_PATH, GY_WEB_URL

driver = webdriver.Chrome(DRIVER_PATH)
# 调整浏览器窗口大小
driver.maximize_window()
sleep(3)
# 打开网址
driver.get('https://www.hupu.com/')
sleep(3)
driver.get('https://bbs.hupu.com/28725765.html')
sleep(3)
driver.get('http://npm.taobao.org/mirrors/chromedriver/75.0.3770.90/')
sleep(3)
# 后退
driver.back()
sleep(3)
# 前进
driver.forward()
sleep(3)
#刷新
driver.refresh()
#
sleep(3)
# 关闭浏览器
driver.close()
#关闭驱动
driver.quit()
