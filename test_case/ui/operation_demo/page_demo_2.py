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
from selenium.webdriver import ActionChains
from selenium.webdriver.common import actions
from selenium.webdriver.common.keys import Keys

from config.conf import DRIVER_PATH



driver = webdriver.Chrome(DRIVER_PATH)
#调整窗口大小
driver.maximize_window()

def get_uri():
    driver.get("D:\\softwareData\\Pycharm\\bulaohu_0728\\demo.html")
def quit_demo():
    driver.quit()

def text_demo():
    #定位元素位置//input[@type='text']
    text = driver.find_element_by_xpath("//input[@type='text']")
    #清空text
    text.clear()
    #输入
    text.send_keys('大白菜')

def file_demo():
    #定位元素位置//input[@type='text']
    file = driver.find_element_by_xpath("//input[@type='file']")
    #清空text
    file.clear()
    #输入
    file.send_keys('C:\\Users\\Administrator\\Desktop\\搜狗截图20190729153211.jpg')

def radio_demo():
    #定位元素位置//input[@type='text']
    radio = driver.find_element_by_xpath("//input[@type='radio'][1]")
    radio.click()

def checkbox_demo():
    #定位元素位置//input[@type='text']
    checkbox1 = driver.find_element_by_xpath("//input[@type='checkbox'][1]")
    checkbox1.click()
    checkbox2 = driver.find_element_by_xpath("//input[@type='checkbox'][2]")
    checkbox2.click()

def password_demo():
    #定位元素位置//input[@type='text']
    password = driver.find_element_by_xpath("//input[@type='password']")
    #清空text
    password.clear()
    #输入
    password.send_keys('csgdvdf')

def number_demo():
    #定位元素位置//input[@type='text']
    number = driver.find_element_by_xpath("//input[@type='number']")
    #清空text
    number.clear()
    #输入
    number.send_keys('123456')

def data_demo():
    js = '''var xpath = '//input[@type="date"]';var element = document.evaluate(xpath,document,null,XPathResult.ANY_TYPE,null).iterateNext();element.setAttribute("value","2019-07-30");'''
    driver.execute_script(js)

def time_demo():
    #定位元素位置//input[@type='text']
    time = driver.find_element_by_xpath("//input[@type='time']")
    #清空text
    time.clear()
    #输入
    time.send_keys('17:30')

def textarea_demo():
    #定位元素位置//input[@type='text']
    textarea = driver.find_element_by_xpath("//textarea")
    #清空text
    textarea.clear()
    #输入
    textarea.send_keys('hello world')

def select_demo():
    #定位元素位置//input[@type='text']
    select = driver.find_element_by_xpath("//select/option[2]")
    select.click()

def a_demo():
    # a = driver.find_element_by_xpath("//a[2]")
    # #输入
    # a.click()
    #精确查找
    # a=driver.find_element_by_link_text('当当')
    # a.click()
    # sleep(2)
    #模糊查询
    text = driver.find_elements_by_partial_link_text('度娘')
    baidu = text
    actions = ActionChains(driver)
    a.key_down(Keys.CONTROL).click(baidu)(Keys.CONTROL)
if __name__ == '__main__':
    get_uri()
    sleep(2)
    text_demo()
    sleep(2)
    file_demo()
    sleep(2)
    radio_demo()
    sleep(2)
    checkbox_demo()
    sleep(2)
    password_demo()
    sleep(2)
    number_demo()
    sleep(2)
    data_demo()
    sleep(2)
    time_demo()
    sleep(2)
    textarea_demo()
    sleep(2)
    select_demo()
    sleep(2)
    a_demo()
    sleep(5)
    driver.quit()
