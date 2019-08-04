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
from time import sleep

from selenium import webdriver

from config.conf import DRIVER_PATH


def open_browser():
    #打开浏览器
    driver = webdriver.Chrome(DRIVER_PATH)
    #调整窗口大小
    driver.maximize_window()
    return driver

def quit_browser(driver):
    #关闭浏览器
    driver.quit()

def text_wenben():
    #打开浏览器
    driver = open_browser()
    sleep(3)
    #打开网址
    driver.get("D:\\softwareData\\Pycharm\\bulaohu_0728\\demo.html")
    sleep(3)
    #定位元素位置//input[@type='text']
    text = driver.find_element_by_xpath("//input[@type='text']")
    #清空text
    text.clear()
    #输入
    text.send_keys('大白菜')
    #获取默认值
    a = text.get_attribute('value')
    print(a)
    sleep(3)
    #关闭浏览器
    quit_browser(driver)


def file_wenben():
    #打开浏览器
    driver = open_browser()
    sleep(3)
    #打开网址
    driver.get("D:\\softwareData\\Pycharm\\bulaohu_0728\\demo.html")
    sleep(3)
    #定位元素位置//input[@type='text']
    file = driver.find_element_by_xpath("//input[@type='file']")
    #清空text
    file.clear()
    #输入
    file.send_keys('C:\\Users\\Administrator\\Desktop\\搜狗截图20190729153211.jpg')
    sleep(3)
    #关闭浏览器
    quit_browser(driver)

if __name__ == '__main__':
    text_wenben()
    file_wenben()


