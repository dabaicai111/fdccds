#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'dabaicai'
__mtime__ = '2019/7/31'
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
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

from config.conf import DRIVER_PATH

driver = webdriver.Chrome(DRIVER_PATH)
#调整窗口大小
driver.maximize_window()

def get_uri():
    driver.get("D:\\softwareData\\Pycharm\\bulaohu_0728\\demo.html")

def open_a():
    baidu = driver.find_element_by_partial_link_text('度娘')
    dd = driver.find_element_by_partial_link_text('当当')
    jd = driver.find_element_by_partial_link_text('京东')
    a = ActionChains(driver)
    a.key_down(Keys.CONTROL).click(baidu).click(dd).click(jd).key_up(Keys.CONTROL).perform()
    sleep(5)
def window_change_demo():
    handles = driver.window_handles
    for h in handles:
        driver.switch_to.window(h)
        sleep(3)
        if(driver.title.__contains__('当当')):
            break

def open_alert():
    driver.find_element_by_xpath("//input[@type='reset']").click()
def alert_alert_demo():
    a = driver.switch_to.alert
    a.accept()

def open_alert1():
    driver.find_element_by_xpath("//input[@type='button']").click()
def alert_alert_demo1():
    a = driver.switch_to.alert
    a.send_keys('nihao')
    # a.dismiss()

if __name__ == '__main__':
    get_uri()
    sleep(3)
    # open_a()
    # window_change_demo()
    # open_alert()
    # sleep(3)
    # alert_alert_demo()
    # sleep(3)
    open_alert1()
    sleep(3)
    alert_alert_demo1()
    sleep(3)
    driver.quit()
