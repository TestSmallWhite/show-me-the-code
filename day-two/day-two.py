#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
题目：做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）？

分析：
    激活码通常都是数字、大小写字母、横线（-）、下划线（_）组成
    长度不等，一般都大于8位，16，32位也有
    唯一性，用于确定用户是否符合要求，激活码是否已经被使用了

    生成激活码大致分为下面几种：
        1.根据设备去生成唯一，guid，uuid等
            优点：
                每个设备的mac是唯一的，所以uuid，guid等都是唯一的
                有现成的模块可以用
            缺点：
                数据库中不好查询，因为是字符串

        2.自己写的纯数字，纯字母的激活码
            优点：
                自己写的，格式好控制
            缺点：
                不好查询
                不能确定唯一，因为量的话有可能出现重复

        3.通过数据库主键生成主键
            优点：
                主键是唯一的，通过和主键有机结合可以生成激活码
                因为是结合主键生成的激活码，在数据库中查询会很快（通过主键）
            缺点：
                无？

实现：
    1.数据库中创建好表
        id（主键，数字）
        key（激活码，字符串：格式：idL-xxxx-yyyy， x和y可以是大小写字母，数字）
        isUse（是否激活，默认为0，1表示使用）
        create_time(创建激活码时间，时间戳)
        use_time（激活时间，时间戳）

    2.能够去数据库中查询id的值，记录起来

    3.根据id去生成激活码

    4.插入到数据库，同时打印到控制台

"""

#每次启动都需要去数据库查询当前id的最大值
#直接查询就好了，不搞什么异步了

#生成数据库操作对象
#我们通过contextlib模块的contextmanager装饰器实现自动获取数据库操作，执行完毕后自动关闭
import mysql.connector
from contextlib import contextmanager
import random, time,string

string.ascii_letters

@contextmanager
def execute_mysql(isCommit = 0):
    conn = mysql.connector.connect(user='root', password='123456', database='show_me_the_code')

    cursor = conn.cursor()

    yield cursor

    cursor.close()

    if isCommit: conn.commit()

    conn.close()


#查询id的最大值
with execute_mysql() as cursor:
    cursor.execute(r'SELECT COUNT(id) FROM day_two')

    global maxNumber

    maxNumber = cursor.fetchone()

    #print(maxNumber[0])
#

# #插入
def insert_jihuoma(count):


    with execute_mysql(1) as cursor:
        # print(r"insert into day_two(`id`, `key`, `isUse`,`createTime`, `useTime`) values(%d, 'xxxxx', 0, '12345789', '987654321')" %(maxNumber))
        for x in range(count):
            print(maxNumber[0] + x)
            cursor.execute(
                r"insert into day_two(`id`, `key`, `isUse`,`createTime`, `useTime`) values(%d, '%s', %d, '%s', '%s')" % (
                maxNumber[0] + x, make_jihuoma(maxNumber[0] + x), 0, str(int(time.time() * 1000000)),  str(int(time.time() * 1000000))))
                #maxNumber[0], make_jihuoma(), '111', '222'))

            #num = num + 1




#设计激活码
"""
前4位是数字+L（大写） + 空格 + ‘-’+ 空格 + 5位数字大小写字母混合
如果id不足4位，补零
例如:0001L - asAD9
"""
def make_jihuoma(id):

    for x in range( 4 - len(str(id))):
        zero =   '0' + str(id)

    #print('zero',zero)
    #print(type(zero))
    qian = zero  + 'L'

    hou = ''

    #1是数字、2是小写字母、3是大写字母
    for y in range(5):
        q = random.randint(0,3)

        if q == 1:
            hou = hou + str(random.randint(0,9))
        elif q == 2:
            hou = hou + str(chr(random.randint(65, 90)))
        else:
            hou = hou + str(chr(random.randint(97, 122)))

    return qian + ' - ' + hou

#获取当前时间戳
#print(str(int(time.time() * 1000000)))
def get_time():
    return str(int(time.time() * 1000000))


#查询是否使用了
def search_isUse(key = None):
    if key :
        with execute_mysql() as cursor:
            cursor.execute(r"select `isUse` from day_two where `key` = '%s'" %(key))
            result = cursor.fetchone()
            return result[0]



#使用激活码
def use_jihuoma(key = None):
    #先检查能不能用
    if search_isUse(key) == 0:
        #print('222')
        with execute_mysql(1) as cursor:
            cursor.execute(r"update day_two set `isUse` = 1, `useTime` = '%s' where `key` = '%s'" %(str(int(time.time() * 1000000)), key))
            #print(r"update day_two set `isUse` = 1, `useTime` = '%s' where key = '%s'" %(str(int(time.time() * 1000000)), key))



print(search_isUse('0459L - 3ajQz'))
