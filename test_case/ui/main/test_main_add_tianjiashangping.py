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

import allure
from tools import assert_tool

@allure.feature('添加商品流程')
@allure.story('登录')
def test_login(base):
    #打开登录界面http://www.qa.yansl.com/#/login
    base.get('打开登录界面','''http://www.qa.yansl.com/#/login''')
    #输入用户名//input[@name='username']
    base.send_keys('输入用户名','''//input[@name='username']''','admin')
    #输入密码//input[@name='password']
    base.send_keys('输入用户名','''//input[@name='password']''','123456')
    #点击登录(//span[contains(text(),'登录')])[1]
    base.click('点击登录','''(//span[contains(text(),'登录')])[1]''')
    #点击残忍拒绝//span[contains(text(),'残忍拒绝')]
    base.click('点击残忍拒绝','''//span[contains(text(),'残忍拒绝')]''')
    #点击登录(//span[contains(text(),'登录')])[1]
    base.click('点击登录','''(//span[contains(text(),'登录')])[1]''')
    sleep(10)
    # f = False
    # try:
    #     base.local_element('//span[text()="首页"]')
    #     f = True
    # except:
    #     pass
    # assert_tool.assert_equal(f,True)
    page_source = base.driver.page_source
    with allure.step('登录页面跳转断言'):
        allure.attach(page_source,'实际结果',allure.attachment_type.TEXT)
        allure.attach('首页','预期结果',allure.attachment_type.TEXT)
    assert_tool.assert_in(page_source,'首页')
    sleep(2)

@allure.feature('添加商品流程')
@allure.story('添加商品')
def test_add_product(base):
    #点击商品(//span[@slot='title'])[1]
    base.click('点击商品','''(//span[@slot='title'])[1]''')
    #点击添加商品//span[contains(text(),'添加商品')]
    base.click('点击添加商品','''//span[contains(text(),'添加商品')]''')
    #点击商品分类//span[@class="el-cascader__label"]
    base.click('点击商品分类','''//span[@class="el-cascader__label"]''')
    #点击服装//li[contains(text(),'服装')]
    base.click('点击服装','''//li[contains(text(),'服装')]''')
    #点击外套//li[contains(text(),'外套')]
    base.click('点击外套','''//li[contains(text(),'外套')]''')
    #输入商品名称//label[text()='商品名称：']/..//div/input
    base.send_keys('输入商品名称','''//label[text()='商品名称：']/..//div/input''','大白菜')
    #输入商品副标题//label[text()='副标题：']/..//div/input
    base.send_keys('输入商品副标题','''//label[text()='副标题：']/..//div/input''','小白菜')
    #点击商品品牌//i[@class="el-select__caret el-input__icon el-icon-arrow-up"]
    base.click('点击商品品牌','''//i[@class="el-select__caret el-input__icon el-icon-arrow-up"]''')
    #点击小米//span[contains(text(),'小米')]
    base.click('点击小米','''//span[contains(text(),'小米')]''')
    #输入商品介绍//textarea[@autosize="true"and@placeholder="请输入内容"]
    base.send_keys('输入商品介绍','''//textarea[@autosize="true"and@placeholder="请输入内容"]''','上海的大白菜')
    #输入商品货号(//input[@type="text"and@autocomplete="off"and@class="el-input__inner"])[5]
    base.send_keys('输入商品货号','''(//input[@type="text"and@autocomplete="off"and@class="el-input__inner"])[5]''','001')
    #输入商品售价(//input[@type="text"and@autocomplete="off"and@class="el-input__inner"])[6]
    base.send_keys('输入商品售价','''(//input[@type="text"and@autocomplete="off"and@class="el-input__inner"])[6]''','5')
    #下拉至最底
    base.scroll_screen('下拉至最底')
    #市场价(//input[@type="text"and@autocomplete="off"and@class="el-input__inner"])[7]
    base.send_keys('市场价','''(//input[@type="text"and@autocomplete="off"and@class="el-input__inner"])[7]''','6')
    #输入商品库存(//input[@type="text"and@autocomplete="off"and@class="el-input__inner"])[8]
    base.send_keys('输入商品库存','''(//input[@type="text"and@autocomplete="off"and@class="el-input__inner"])[8]''','100')
    #计量单位(//input[@type="text"and@autocomplete="off"and@class="el-input__inner"])[9]
    base.send_keys('计量单位','''(//input[@type="text"and@autocomplete="off"and@class="el-input__inner"])[9]''','斤')
    #输入商品重量(//input[@type="text"and@autocomplete="off"and@class="el-input__inner"])[10]
    base.send_keys('输入商品重量','''(//input[@type="text"and@autocomplete="off"and@class="el-input__inner"])[10]''','3')
    #排序(//input[@type="text"and@autocomplete="off"and@class="el-input__inner"])[11]
    base.send_keys('排序','''(//input[@type="text"and@autocomplete="off"and@class="el-input__inner"])[11]''','01')
    #点击下一步，填写商品促销//span[contains(text(),'下一步，填写商品促销')]
    base.click('点击下一步，填写商品促销','''//span[contains(text(),'下一步，填写商品促销')]''')
    sleep(2)

@allure.feature('添加商品流程')
@allure.story('填写商品促销')
#点击下一步，填写商品属性//span[contains(text(),'下一步，填写商品属性')]
def test_add_product_abc(base):
    base.scroll_screen('下拉至最底')
    base.click('点击下一步，填写商品属性','''//span[contains(text(),'下一步，填写商品属性')]''')
    sleep(2)

@allure.feature('添加商品流程')
@allure.story('填写商品属性')
#点击下一步，选择商品关联//span[contains(text(),'下一步，选择商品关联')]
#下拉至最底
def test_add_product_cd(base):
    base.scroll_screen('下拉至最底')
    base.click('点击下一步，选择商品关联','''//span[contains(text(),'下一步，选择商品关联')]''')
    sleep(2)

@allure.feature('添加商品流程')
@allure.story('选择商品关联')
#下拉至最底
#点击完成，提交商品//span[contains(text(),'完成，提交商品')]
def test_add_product_ef(base):
    base.scroll_screen('下拉至最底')
    base.click('点击完成，提交商品','''//span[contains(text(),'完成，提交商品')]''')
    sleep(2)

    #点击确定//span[contains(text(),'确定')]
    base.scroll_screen('下拉至最底')
    base.click('点击确定','''//span[contains(text(),'确定')]''')
    sleep(3)
    pass

