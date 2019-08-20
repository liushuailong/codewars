# -*- coding: utf-8 -*-

# print 打印带有颜色的信息
# 以 f开头表示在字符串内支持大括号内的python 表达式


def esc(code=0):
    return f'[{code}m'


# print(esc('31;1;0') + 'Error:' + esc() + 'important')

# 在python中使用定时器


import schedule
import time


def job():
    print("I`m working...")


schedule.every(10).minutes.do(job)
schedule.every().hour.do(job)
schedule.every().day.at("16:39").do(job)
schedule.every().monday.do(job)
schedule.every().wednesday.at("13:15").do(job)
schedule.every().minute.at(":17").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)




