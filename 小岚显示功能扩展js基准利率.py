#! /usr/bin/python
# -*- coding:utf-8 -*-


from pyecharts import Line, Bar
import re


irs_a_1, irs_a_2 = float(0.011), float(0.013)
irs_a_3, irs_a_4, irs_a_5 = float(0.015), float(0.021), float(0.0275)
irs_b_1, irs_b_2, irs_b_3 = float(0.0435), float(0.0475), float(0.0490)
irs_c_1, irs_c_2 = float(0.0275), float(0.0325)
irs_a_name = ["三个月", "半年", "一年", "两年", "三年", "五年以内", "五年以上"]
irs_a = [irs_a_1, irs_a_2, irs_a_3, irs_a_4, irs_a_5, None, None]
irs_b_name = ["三个月", "半年", "一年", "两年", "三年", "五年以内", "五年以上"]
irs_b = [None, None, irs_b_1, None, None, irs_b_2, irs_b_3]
irs_c_name = ["三个月", "半年", "一年", "两年", "三年", "五年以内", "五年以上"]
irs_c = [None, None, None, None, None, irs_c_1, irs_c_2]


def bir_name():
    print("自定义名称，这是种花家的效验机制……")
    global file_name
    while True:
        file_name = str(input("该项将决定图表名称和文件名称\n" + "该图名称为："))
        if file_name.replace(' ', '') == '':
            print("未命名的图表，将不能创建对应的文件！\n" + "效验名称失败！")
            print("\n重新效验名称……")
        else:
            print("\t命名验证通过！")
            break
    return file_name


def bir_quadrant_1():
    bir_quadrant_one = str(input("第一象限名称："))
    return bir_quadrant_one


def bir_quadrant_2():
    bir_quadrant_two = str(input("第二象限名称："))
    return bir_quadrant_two


def bir_quadrant_3():
    bir_quadrant_three = str(input("第三象限名称："))
    return bir_quadrant_three


def bir():
    print("生成js源码中……")
    line = Line("{}".format(bir_name()))
    line.add("{}".format(bir_quadrant_1()),
             irs_a_name,
             irs_a,
             is_fill=True,
             area_color='EED5B7',
             area_opacity=0.4,
             is_smooth=True)
    line.add("{}".format(bir_quadrant_2()),
             irs_b_name,
             irs_b,
             is_fill=True,
             area_color='#1C86EE',
             area_opacity=0.3,
             is_smooth=True)
    line.add("{}".format(bir_quadrant_3()),
             irs_c_name,
             irs_c, is_fill=True,
             area_color='#FF0000',
             area_opacity=0.5,
             is_smooth=True,
             is_more_utils=True)
    line_name = input("存放图表的文件名：")
    line.render("{}.html".format(line_name))
    print("js源码生成完毕……\n")
