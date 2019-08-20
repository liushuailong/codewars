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

#while True:
#    schedule.run_pending()
#    time.sleep(1)

from time import sleep


def progress(percent=0, width=30):
    left = width * percent // 100
    right = width - left
    print("[", "#" * left, " " * right, "]", f" {percent:.0f}%", sep="", end="", flush=True)


# for i in range(101):
#     progress(i)
#     sleep(0.1)


import json
my_mapping = {"a": 23, "b": 42, "c": 0xc0ffee}
print(json.dumps(my_mapping, indent=4, sort_keys=True))
import pprint
my_mapping = [{"a": 23, "b": 42, "c": 0xc0ffee}, {"a": 231, "b": 42, "c": 0xc0ffee}]
pprint.pprint(my_mapping, width=4)
