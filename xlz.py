#! /usr/bin/python
# -*- coding:utf-8 -*-


import sys
import os
from xldef import *
from 小岚显示功能扩展js基准利率 import *


def rabbit_purple_radish():
    one_type = input("\n一表看一年，才知没有钱~\n此功能用于基础图表显示\n")
    while True:
        if one_type == '基准利率':
            map_show()
            break
        elif one_type == '退出':
            print("正在结束该功能！")
            break
        elif one_type.replace(' ', '') == '':
            one_type = input("想看什么图？兔仔我画给你看！" + "\n不说话我就不开心！")
            continue
        print("已关闭此功能！")


def rabbit_radish():
    while True:
        one_type = input("\n这次萝卜要放哪呢？   ")
        if one_type == '放老家':
            try:
                deposit_str = float(input('-' * 100 + "\n给小岚多少萝卜？       "))
                deposit_time = float(input('-' * 100 + "\n要放多久？     "))
            except ValueError:
                print('-' * 100 + "存就要放萝卜哦！")
            else:
                list_time_deposit(deposit_str, deposit_time)
                continue
        elif one_type == '贷款萝卜':
            try:
                loan_str = float(input('-' * 100 + "\n贷多少？      "))
                loan_time = float(input('-' * 100 + "\n什么时候还？       "))
            except ValueError:
                print('-' * 100 + "说清楚贷多少萝卜哦！")
            else:
                list_time_loan(loan_str, loan_time)
                continue
        elif one_type == '买窝用':
            try:
                cpf_str = float(input('-' * 100 + "\n贷多少？       "))
                cpf_time = float(input('-' * 100 + "\n什么时候还？        "))
            except ValueError:
                print("既然想有窝，萝卜是不可少的！")
            else:
                list_time_cpf(cpf_str, cpf_time)
                continue
        else:
            if one_type == '离开':
                print("谢谢！小岚会更好！@发现美的眼睛赶紧变优秀！")
                break
            elif one_type == '历史萝卜':
                    print("\n小岚提示\n\t\t___无称不成率，无较不成利___")
                    print(time_list_stamp)
            else:
                print("\t要么亲没说对，要么...")
                print("\t反正不是小岚的错！")


def rabbit_white_radish():
    while True:
        two_type = input("这可是小岚的拿手本领！好看的萝卜表，有趣的动画！\n" + "需要生成什么样的萝卜表？ ")
        if two_type == '基准利率':
            bir()
        elif two_type == '历年利率':
            pass
        elif two_type == '重新输入':
            continue
        else:
            if two_type == '计算':
                print("该功能正在关闭，稍后跳转到计算功能中……")
            break



# 对历史数据进行加密处理
# 编写数据组，格式化输出历史数据


def plus_wall():
    rabbit_purple_radish()
    rabbit_radish()
    rabbit_white_radish()
