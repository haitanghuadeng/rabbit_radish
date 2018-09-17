#! /usr/bin/python
# -*- coding:utf-8 -*-


import time


irs_a_1, irs_a_2 = float(0.011), float(0.013)
irs_a_3, irs_a_4, irs_a_5 = float(0.015), float(0.021), float(0.0275)
irs_b_1, irs_b_2, irs_b_3 = float(0.0435), float(0.0475), float(0.0490)
irs_c_1, irs_c_2 = float(0.0275), float(0.0325)
irs_a = [irs_a_1, irs_a_2, irs_a_3, irs_a_4, irs_a_5]
irs_b = [irs_b_1, irs_b_2, irs_b_3]
irs_c = [irs_c_1, irs_c_2]
time_list_stamp = []   # 子进程时间记录仪

def map_show():
    m = [['城乡居民和单位存款', "利率 % （单位/百分比）"],
         ['活期存款', "0.35"],
         ['整存整取定期存款', '选项'],
         ['三个月', '1.1'], ['半年', '1.3'], ['一年', '1.5'],  ['两年', '2.1'], ['三年', '2.75'],
         ['各项存贷', '选项'],
         ['一年以内（含一年）', '4.35'], ['五年以内（含五年）', '4.75'], ['五年以上', '4.90'],
         ['个人住房公积金贷款', '选项'],
         ['五年以内（含五年）', '2.75'], ['五年以上', '3.25'],
         ['暂无额外', '选项']]
    for mm in m:
        print('-' * 100)
        print("\n\t{0:{2}^20}\t{1:{2}^30}".format(mm[0], mm[1], chr(12288)))


# PEP8规范中声明，形参变量名不应与外部变量名同名
# 拆分函数，其作用于防止各个功能计算函数时，发生错误ALG计算结果
def alg_a(deposit_str, irs_aa):
    result = deposit_str * irs_aa * 1
    return print("萝卜利息为: %s" % result)


def alg_l(loan_str, irs_bb):
    result = loan_str * irs_bb * 1
    return print("萝卜利息为: %s" % result)


def alg_c(cpf_str, irs_cc):
    result = cpf_str * irs_cc * 1
    return print("萝卜利息为: %s" % result)


def list_time_deposit(deposit_str, deposit_time):

    if deposit_time == 3:
        alg_a(deposit_str, irs_a[0])
    elif deposit_time == 6:
        alg_a(deposit_str, irs_a[1])
    elif deposit_time == 12:
        alg_a(deposit_str, irs_a[2])
    elif deposit_time == 24:
        alg_a(deposit_str, irs_a[3])
    elif deposit_time == 36:
        alg_a(deposit_str, irs_a[4])
    else:
        print("\t注意啦！整取时间只能是规定的哦！最好吃的萝卜一定是成熟的！")
        print("\t小岚提醒您，兔子家的存款是要符合萝卜入坑规则哦！")
    time1 = time.localtime(time.time())
    time_deposit_dot = ["本次萝卜坑：整存整取定期存款",
                        "存萝卜￥：{}".format(deposit_str),
                        "放多长呢？：{}".format(deposit_time),
                        "啥时呢？{}年{}月{}日{}是{}分{}秒"
                        .format(time1[0], time1[1], time1[2], time1[3], time1[4], time1[5])]
    return time_list_stamp.append(time_deposit_dot)


def list_time_loan(loan_str, loan_time):
    if loan_time <= 1:
        alg_l(loan_str, irs_b[0])
    elif loan_time > 1 <= 5:
        alg_l(loan_str, irs_b[1])
    elif loan_time > 5:
        alg_l(loan_str, irs_b[2])
    else:
        print("贷款时间 {} 输入值存在异常".format(loan_time))
    time2 = time.localtime(time.time())
    time_loan_dot = ["本次萝卜坑：各项贷款",
                     "存萝卜￥：{}".format(loan_str),
                     "放多长呢？：{}".format(loan_time),
                     "啥时呢？{}年{}月{}日{}是{}分{}秒"
                     .format(time2[0], time2[1], time2[2], time2[3], time2[4], time2[5])]
    return time_list_stamp.append(time_loan_dot)


def list_time_cpf(cpf_str, cpf_time):
    if cpf_time <= 5:
        alg_c(cpf_str, irs_c[0])
    elif cpf_time > 5:
        alg_c(cpf_str, irs_c[1])
    time3 = time.localtime(time.time())
    time_cpf_dot = ["本次萝卜坑：个人住房公积金贷款",
                    "存萝卜￥{}".format(cpf_str),
                    "放多长呢？：{}".format(cpf_time),
                    "啥时呢？{}年{}月{}日{}是{}分{}秒"
                    .format(time3[0], time3[1], time3[2], time3[3], time3[4], time3[5])]
    return time_list_stamp.append(time_cpf_dot)
