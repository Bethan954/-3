# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/6/30 8:36
# @Author : Perla
# @Email : 13896934450@163.com
# @File : gmjj.py
# @Software: PyCharm

import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
from matplotlib import colors

# plt.style.use('ggplot')
mpl.rc("font", family='YouYuan')
color = list(colors.CSS4_COLORS.values())


# 采购经理人指数
def pmi():
    df_PMI = pd.read_csv("data/gmjj/PMI.csv")

    plt.figure(figsize=(20, 10), dpi=100)
    mpl.rcParams['axes.unicode_minus'] = False

    month = df_PMI['Montth'].tolist()
    Manufacturing_YOY = df_PMI['Manufacturing_YOY'].tolist()
    Nonmanufacturing_YOY = df_PMI['Nonmanufacturing_YOY'].tolist()
    for i in range(len(Manufacturing_YOY)):
        if Manufacturing_YOY[i][0] == '-':
            Manufacturing_YOY[i] = float(Manufacturing_YOY[i][1:-1]) * (-1)
        else:
            Manufacturing_YOY[i] = float(Manufacturing_YOY[i][:-1])
        if Nonmanufacturing_YOY[i][0] == '-':
            Nonmanufacturing_YOY[i] = float(Nonmanufacturing_YOY[i][1:-1]) * (-1)
        else:
            Nonmanufacturing_YOY[i] = float(Nonmanufacturing_YOY[i][:-1])

    month.reverse()
    Manufacturing_YOY.reverse()
    Nonmanufacturing_YOY.reverse()
    plt.plot(month[108:], Manufacturing_YOY[108:], c='Salmon', marker='.', label="制造业同比增长(%)")
    plt.plot(month[108:], Nonmanufacturing_YOY[108:], c='SkyBlue', marker='*', linestyle='--', label="非制造业同比增长(%)")
    plt.legend(loc='best')
    plt.ylim(-50, 80)

    plt.text('2020年02月份', -27.44 + 1, '-27.44%', ha='left', va='bottom', fontsize=24, color='Salmon', family='SimHei')
    plt.text('2020年02月份', -27.44, '·', ha='center', va='center', fontsize=20, color='Salmon')
    plt.text('2020年02月份', -45.49, '·', ha='center', va='center', fontsize=20, color='SkyBlue')
    plt.text('2020年02月份', -45.49 - 2, '-45.49%', ha='left', va='bottom', fontsize=24, color='SkyBlue', family='SimHei')
    plt.text('2021年02月份', 50.6 + 2, '50.6%', ha='left', va='bottom', fontsize=24, color='Salmon', family='SimHei')
    plt.text('2021年02月份', 50.6, '·', ha='center', va='center', fontsize=20, color='Salmon')
    plt.text('2021年02月份', 73.65, '·', ha='center', va='center', fontsize=20, color='SkyBlue')
    plt.text('2021年02月份', 73.65 - 6, '73.65%', ha='left', va='bottom', fontsize=24, color='SkyBlue', family='SimHei')

    plt.text('2019年12月份', 76, '2019年12月份', ha='center', va='center', fontsize=20, color='darkred', family='SimHei')
    plt.vlines('2019年12月份', 74, -47, colors="darkred", linestyles="dashed")

    plt.gca().xaxis.set_major_locator(ticker.MultipleLocator(12))
    plt.xlabel("年份", fontdict={'size': 20})
    plt.ylabel("数据", fontdict={'size': 20})
    plt.xticks(size=20)
    plt.yticks(size=20)

    plt.title("PMI", fontdict={'size': 20})
    ax = plt.gca();  # 获得坐标轴的句柄
    ax.spines['bottom'].set_linewidth(2);  ###设置底部坐标轴的粗细
    ax.spines['left'].set_linewidth(2);  ####设置左边坐标轴的粗细
    ax.spines['right'].set_linewidth(2);  ###设置右边坐标轴的粗细
    ax.spines['top'].set_linewidth(2);  ####设置上部坐标轴的粗细
    plt.savefig('pic/PMI.png')
    plt.show()


# 中国居民消费指数
def cpi():
    df_cpi = pd.read_csv("data/gmjj/CPI.csv")  # 08-22年间，每月中国居民消费价格指数
    plt.figure(figsize=(20, 10), dpi=100)

    Month = df_cpi['Month'].tolist()
    Nation_Current_Month = df_cpi['Nation_Current_Month'].tolist()
    City_Current_Month = df_cpi['City_Current_Month'].tolist()
    Country_Current_Month = df_cpi['Country_Current_Month'].tolist()

    Month.reverse()
    Nation_Current_Month.reverse()
    City_Current_Month.reverse()
    Country_Current_Month.reverse()

    plt.plot(Month[108:], Nation_Current_Month[108:], c='LightCoral', marker='.', label="全国")
    plt.plot(Month[108:], City_Current_Month[108:], c='SkyBlue', marker='.', label="城市")
    plt.plot(Month[108:], Country_Current_Month[108:], c='Turquoise', marker='.', label="农村")
    plt.legend(loc='best')

    plt.text('2020年11月份', 99.5 - 0.2, 99.5, ha='right', va='bottom', fontsize=24, color='LightCoral', family='SimHei')
    plt.text('2020年11月份', 99.5, '·', ha='center', va='center', fontsize=20, color='LightCoral')
    plt.text('2020年11月份', 99.6, '·', ha='center', va='center', fontsize=20, color='SkyBlue')
    plt.text('2020年11月份', 99.6 + 0.5, 99.6, ha='center', va='bottom', fontsize=24, color='SkyBlue', family='SimHei')
    plt.text('2020年11月份', 99.2 - 0.6, 99.2, ha='left', va='bottom', fontsize=24, color='Turquoise', family='SimHei')
    plt.text('2020年11月份', 99.2, '·', ha='center', va='center', fontsize=20, color='Turquoise')

    plt.text('2019年12月份', 109, '2019年12月份', ha='center', va='center', fontsize=20, color='darkred', family='SimHei')
    plt.vlines('2019年12月份', 109, 95, colors="darkred", linestyles="dashed")

    plt.gca().xaxis.set_major_locator(ticker.MultipleLocator(12))
    plt.xlabel("年份", fontdict={'size': 16})
    plt.ylabel("数据", fontdict={'size': 16})
    plt.title("CPI", fontdict={'size': 20})

    plt.xticks(size=20)
    plt.yticks(size=20)

    ax = plt.gca();  # 获得坐标轴的句柄
    ax.spines['bottom'].set_linewidth(2);  ###设置底部坐标轴的粗细
    ax.spines['left'].set_linewidth(2);  ####设置左边坐标轴的粗细
    ax.spines['right'].set_linewidth(2);  ###设置右边坐标轴的粗细
    ax.spines['top'].set_linewidth(2);  ####设置上部坐标轴的粗细
    plt.savefig('pic/CPI.png')
    plt.show()


# 中国消费者信心指数
def cci():
    df_cci = pd.read_csv("data/gmjj/CCI.csv")  # 07-21年间，中国消费者信心指数数据
    """
    同比增长
    """
    plt.figure(figsize=(20, 10), dpi=100)

    Month = df_cci['Month'].tolist()
    CCI_YOY = df_cci['CCI_YOY'].tolist()
    CSI_YOY = df_cci['CSI_YOY'].tolist()
    CEI_YOY = df_cci['CEI_YOY'].tolist()

    for i in range(len(CCI_YOY)):
        if CCI_YOY[i][0] == '-':
            CCI_YOY[i] = float(CCI_YOY[i][1:-1]) * (-1)
        else:
            CCI_YOY[i] = float(CCI_YOY[i][:-1])
        if CSI_YOY[i][0] == '-':
            CSI_YOY[i] = float(CSI_YOY[i][1:-1]) * (-1)
        else:
            CSI_YOY[i] = float(CSI_YOY[i][:-1])
        if CEI_YOY[i][0] == '-':
            CEI_YOY[i] = float(CEI_YOY[i][1:-1]) * (-1)
        else:
            CEI_YOY[i] = float(CEI_YOY[i][:-1])

    Month.reverse()
    CCI_YOY.reverse()
    CSI_YOY.reverse()
    CEI_YOY.reverse()

    plt.plot(Month[108:], CCI_YOY[108:], c='LightCoral', marker='.', label="消费者信心同比增长")
    plt.plot(Month[108:], CSI_YOY[108:], c='SkyBlue', marker='.', label="消费者满意同比增长")
    plt.plot(Month[108:], CEI_YOY[108:], c='Turquoise', marker='.', label="消费者预期同比增长")
    plt.legend(loc='best')

    plt.text('2020年06月份', -10.56, '-10.56%', ha='left', va='bottom', fontsize=24, color='LightCoral', family='SimHei')
    plt.text('2020年06月份', -10.56, '·', ha='center', va='center', fontsize=20, color='LightCoral')
    plt.text('2020年06月份', -9.7, '·', ha='center', va='center', fontsize=20, color='SkyBlue')
    plt.text('2020年06月份', -9.7 + 1, '-9.7%', ha='left', va='bottom', fontsize=24, color='SkyBlue', family='SimHei')
    plt.text('2020年06月份', -11.5 - 1.5, '-11.5%', ha='left', va='bottom', fontsize=24, color='Turquoise',
             family='SimHei')
    plt.text('2020年06月份', -11.5, '·', ha='center', va='center', fontsize=20, color='Turquoise')

    plt.text('2019年12月份', 21, '2019年12月份', ha='center', va='center', fontsize=20, color='darkred', family='SimHei')
    plt.vlines('2019年12月份', 20, -15, colors="darkred", linestyles="dashed")

    plt.gca().xaxis.set_major_locator(ticker.MultipleLocator(10))
    plt.xlabel("年份", fontdict={'size': 16})
    plt.ylabel("数据", fontdict={'size': 16})
    plt.title("CCI", fontdict={'size': 20})
    plt.xticks(size=20)
    plt.yticks(size=20)

    ax = plt.gca();  # 获得坐标轴的句柄
    ax.spines['bottom'].set_linewidth(2);  ###设置底部坐标轴的粗细
    ax.spines['left'].set_linewidth(2);  ####设置左边坐标轴的粗细
    ax.spines['right'].set_linewidth(2);  ###设置右边坐标轴的粗细
    ax.spines['top'].set_linewidth(2);  ####设置上部坐标轴的粗细
    plt.savefig('pic/CCI.png')
    plt.show()


# 中国财政收入数据
def Fiscal_Revenue():
    df_Fiscal_Revenue = pd.read_csv("data/gmjj/Fiscal_Revenue.csv")  # 08-21年间，每月中国财政收入数据
    import numpy as np
    plt.figure(figsize=(20, 10), dpi=100)

    Month = df_Fiscal_Revenue['Month'].tolist()
    Current_Month_Value = df_Fiscal_Revenue['Current_Month_Value'].tolist()
    Current_Month_YOY = df_Fiscal_Revenue['Current_Month_YOY'].tolist()

    for i in range(len(Current_Month_Value)):
        if Current_Month_Value[i] == 0:
            Current_Month_Value[i] = np.NAN
        if Current_Month_YOY[i][0] == '-':
            Current_Month_YOY[i] = float(Current_Month_YOY[i][1:-1]) * (-1)
        else:
            Current_Month_YOY[i] = float(Current_Month_YOY[i][:-1])

    Month.reverse()
    Current_Month_Value.reverse()
    Current_Month_YOY.reverse()

    # plt.plot(Month, Current_Month_Value, c='Salmon', marker='.', label="当月(亿元)")
    plt.plot(Month[132:], Current_Month_YOY[132:], c='Salmon', marker='.', label="同比增长")
    plt.legend(loc='best')

    plt.text('2020年03月份', -26.11, '-26.11%', ha='left', va='bottom', fontsize=24, color='Salmon', family='SimHei')
    plt.text('2020年03月份', -26.11, '·', ha='center', va='center', fontsize=20, color='Salmon')
    plt.text('2021年03月份', 42.39 - 3, '42.39%', ha='left', va='bottom', fontsize=24, color='Salmon', family='SimHei')
    plt.text('2021年03月份', 42.39, '·', ha='center', va='center', fontsize=20, color='Salmon')

    plt.text('2019年12月份', 43, '2019年12月份', ha='center', va='center', fontsize=20, color='darkred', family='SimHei')
    plt.vlines('2019年12月份', 42, -30, colors="darkred", linestyles="dashed")

    plt.gca().xaxis.set_major_locator(ticker.MultipleLocator(12))
    plt.xlabel("年份", fontdict={'size': 16})
    plt.ylabel("数据", fontdict={'size': 16})
    plt.title("Fiscal_Revenue", fontdict={'size': 20})

    plt.xticks(size=20)
    plt.yticks(size=20)

    ax = plt.gca();  # 获得坐标轴的句柄
    ax.spines['bottom'].set_linewidth(2);  ###设置底部坐标轴的粗细
    ax.spines['left'].set_linewidth(2);  ####设置左边坐标轴的粗细
    ax.spines['right'].set_linewidth(2);  ###设置右边坐标轴的粗细
    ax.spines['top'].set_linewidth(2);  ####设置上部坐标轴的粗细
    plt.savefig('pic/Fiscal_Revenue.png')
    plt.show()


# 每季度中国全国税收收入
def National_Tax_Revenue():
    df_National_Tax_Revenue = pd.read_csv("data/gmjj/National_Tax_Revenue.csv")  # 08-21年间，每月中国财政收入数据
    import numpy as np
    plt.figure(figsize=(20, 10), dpi=100)

    Quarter = df_National_Tax_Revenue['Quarter'].tolist()
    YOY = df_National_Tax_Revenue['YOY'].tolist()

    for i in range(len(YOY)):
        if YOY[i][-1] != '%':
            YOY[i] = np.NAN
        else:
            YOY[i] = float(YOY[i][:-1])

    Quarter.reverse()
    YOY.reverse()

    # plt.plot(Month, Current_Month_Value, c='Salmon', marker='.', label="当月(亿元)")
    plt.plot(Quarter, YOY, c='Salmon', marker='.', label="较上年同期(%)")
    plt.legend(loc='best')

    plt.text('2020年1季度', -16.4, '-16.4%', ha='left', va='bottom', fontsize=24, color='Salmon', family='SimHei')
    plt.text('2020年1季度', -16.4, '·', ha='center', va='center', fontsize=20, color='Salmon')

    plt.text('2019年1-4季度', 38, '2019年1-4季度', ha='center', va='center', fontsize=20, color='darkred', family='SimHei')
    plt.vlines('2019年1-4季度', 37, -20, colors="darkred", linestyles="dashed")

    plt.gca().xaxis.set_major_locator(ticker.MultipleLocator(12))
    plt.xlabel("年份", fontdict={'size': 16})
    plt.ylabel("数据", fontdict={'size': 16})
    plt.title("National_Tax_Revenue", fontdict={'size': 20})
    plt.xticks(size=20)
    plt.yticks(size=20)

    ax = plt.gca();  # 获得坐标轴的句柄
    ax.spines['bottom'].set_linewidth(2);  ###设置底部坐标轴的粗细
    ax.spines['left'].set_linewidth(2);  ####设置左边坐标轴的粗细
    ax.spines['right'].set_linewidth(2);  ###设置右边坐标轴的粗细
    ax.spines['top'].set_linewidth(2);  ####设置上部坐标轴的粗细
    plt.savefig('pic/National_Tax_Revenue.png')
    plt.show()


# 每季度中国国内生产总值
def gdp():
    df_GDP = pd.read_csv("data/gmjj/GDP.csv")  # 08-20年间，每月中国外商直接投资数据
    # df_GDP
    plt.figure(figsize=(20, 10), dpi=100)

    Quater = df_GDP['Quater'].tolist()[:-16]
    GDP_YOY = df_GDP['GDP_YOY'].tolist()[:-16]
    Primary_Indusry_YOY = df_GDP['Primary_Indusry_YOY'].tolist()[:-16]
    Secondary_Indusry_YOY = df_GDP['Secondary_Indusry_YOY'].tolist()[:-16]
    Tertiary_Indusry_YOY = df_GDP['Tertiary_Indusry_YOY'].tolist()[:-16]
    for i in range(len(GDP_YOY)):
        GDP_YOY[i] = float(GDP_YOY[i][:-1])
        Primary_Indusry_YOY[i] = float(Primary_Indusry_YOY[i][:-1])
        Secondary_Indusry_YOY[i] = float(Secondary_Indusry_YOY[i][:-1])
        Tertiary_Indusry_YOY[i] = float(Tertiary_Indusry_YOY[i][:-1])

    Quater.reverse()
    GDP_YOY.reverse()
    Primary_Indusry_YOY.reverse()
    Secondary_Indusry_YOY.reverse()
    Tertiary_Indusry_YOY.reverse()

    plt.plot(Quater[8:], GDP_YOY[8:], c='Salmon', marker='.', label="国内生产总值同比增长")
    plt.plot(Quater[8:], Primary_Indusry_YOY[8:], c='Turquoise', marker='.', label="第一产业同比增长")
    plt.plot(Quater[8:], Secondary_Indusry_YOY[8:], c='SkyBlue', marker='.', label="第二产业同比增长")
    plt.plot(Quater[8:], Tertiary_Indusry_YOY[8:], c='plum', marker='.', label="第三产业同比增长")
    plt.legend(loc='best')

    # 最小值
    plt.text('2020年第1季度', -6.8 - 1, '-6.8%', ha='left', va='bottom', fontsize=24, color='Salmon', family='SimHei')
    plt.text('2020年第1季度', -6.8, '·', ha='center', va='center', fontsize=20, color='Salmon')
    plt.text('2020年第1季度', -3.2, '·', ha='center', va='center', fontsize=20, color='Turquoise')
    plt.text('2020年第1季度', -3.2, '-3.2%', ha='left', va='bottom', fontsize=24, color='Turquoise', family='SimHei')
    plt.text('2020年第1季度', -9.6, '·', ha='center', va='center', fontsize=20, color='SkyBlue')
    plt.text('2020年第1季度', -9.6 - 1, '-9.6%', ha='left', va='bottom', fontsize=24, color='SkyBlue', family='SimHei')
    plt.text('2020年第1季度', -5.2, '·', ha='center', va='center', fontsize=20, color='plum')
    plt.text('2020年第1季度', -5.2, '-5.2%', ha='left', va='bottom', fontsize=24, color='plum', family='SimHei')
    # 最大值
    plt.text('2021年第1季度', 18.3 + 0.5, '18.3%', ha='left', va='bottom', fontsize=24, color='Turquoise', family='SimHei')
    plt.text('2021年第1季度', 18.3, '·', ha='center', va='center', fontsize=20, color='Salmon')
    plt.text('2021年第1季度', 8.1, '·', ha='center', va='center', fontsize=20, color='Turquoise')
    plt.text('2021年第1季度', 8.1 + 0.5, '8.1%', ha='left', va='bottom', fontsize=24, color='Turquoise', family='SimHei')
    plt.text('2021年第1季度', 24.4, '·', ha='center', va='center', fontsize=20, color='SkyBlue')
    plt.text('2021年第1季度', 24.4 + 0.5, '24.4%', ha='left', va='bottom', fontsize=24, color='SkyBlue', family='SimHei')
    plt.text('2021年第1季度', 15.6, '·', ha='center', va='center', fontsize=20, color='plum')
    plt.text('2021年第1季度', 15.6 + 0.5, '15.6%', ha='left', va='bottom', fontsize=24, color='plum', family='SimHei')

    plt.text('2019年第1-4季度', 26, '2019年第1-4季度', ha='center', va='center', fontsize=20, color='darkred', family='SimHei')
    plt.vlines('2019年第1-4季度', 25, -17, colors="darkred", linestyles="dashed")

    plt.gca().xaxis.set_major_locator(ticker.MultipleLocator(6))
    plt.xlabel("年份", fontdict={'size': 16})
    plt.ylabel("数据（%）", fontdict={'size': 16})
    plt.title("GDP", fontdict={'size': 20})
    plt.xticks(size=16)
    plt.yticks(size=16)

    ax = plt.gca();  # 获得坐标轴的句柄
    ax.spines['bottom'].set_linewidth(2);  # 设置底部坐标轴的粗细
    ax.spines['left'].set_linewidth(2);  # 设置左边坐标轴的粗细
    ax.spines['right'].set_linewidth(2);  # 设置右边坐标轴的粗细
    ax.spines['top'].set_linewidth(2);  # 设置上部坐标轴的粗细
    plt.savefig('pic/GDP.png')
    plt.show()


# 中国油价调整数据
def Gas_Price():
    df_Gas_Price = pd.read_csv("data/gmjj/Gas_Price.csv")  # 00-22年间，中国油价调整数据
    plt.figure(figsize=(20, 10), dpi=100)

    Adjust_Date = df_Gas_Price['Adjust_Date'].tolist()
    Gas_Price = df_Gas_Price['Gas_Price'].tolist()
    Diesel_Price = df_Gas_Price['Diesel_Price'].tolist()

    Adjust_Date.reverse()
    Gas_Price.reverse()
    Diesel_Price.reverse()

    plt.plot(Adjust_Date[108:], Gas_Price[108:], c='Salmon', marker='.', label="汽油价格(元/吨)")
    plt.plot(Adjust_Date[108:], Diesel_Price[108:], c='SkyBlue', marker='.', label="柴油价格(元/吨)")
    plt.legend(loc='best')

    plt.text('2020/11/6', 6000 - 300, 6000, ha='center', va='bottom', fontsize=20, color='Salmon', family='SimHei')
    plt.text('2020/11/6', 6000, '*', ha='center', va='center', fontsize=20, color='Salmon', family='SimHei')
    plt.text('2020/11/6', 5075 - 300, 5075, ha='center', va='bottom', fontsize=20, color='SkyBlue', family='SimHei')
    plt.text('2020/11/6', 5075, '*', ha='center', va='center', fontsize=20, color='SkyBlue', family='SimHei')

    plt.text('2019/12/3', 10000, '2019/12/3', ha='center', va='center', fontsize=20, color='darkred', family='SimHei')
    plt.vlines('2019/12/3', 10000, 0.5, colors="darkred", linestyles="dashed")

    plt.gca().xaxis.set_major_locator(ticker.MultipleLocator(15))
    plt.xlabel("年份", fontdict={'size': 16})
    plt.ylabel("数据（%）", fontdict={'size': 16})
    plt.title("Gas_Price", fontdict={'size': 20})
    plt.xticks(size=20)
    plt.yticks(size=20)

    ax = plt.gca();  # 获得坐标轴的句柄
    ax.spines['bottom'].set_linewidth(2);  ###设置底部坐标轴的粗细
    ax.spines['left'].set_linewidth(2);  ####设置左边坐标轴的粗细
    ax.spines['right'].set_linewidth(2);  ###设置右边坐标轴的粗细
    ax.spines['top'].set_linewidth(2);  ####设置上部坐标轴的粗细
    plt.savefig('pic/Gas_Price.png')
    plt.show()


# 每季度中国企业景气及企业家信心指数
def Enterprise_Confidence():
    df_Enterprise_Confidence = pd.read_csv("data/gmjj/Enterprise_Confidence.csv")  # 00-22年间，中国油价调整数据
    plt.figure(figsize=(20, 10), dpi=100)

    Quarter = df_Enterprise_Confidence['Quarter'].tolist()
    Climate_Index_Enterprise = df_Enterprise_Confidence['Climate_Index_Enterprise'].tolist()
    Macro_econ_Climate_Index = df_Enterprise_Confidence['Macro_econ_Climate_Index'].tolist()
    for i in range(len(Climate_Index_Enterprise)):
        if Climate_Index_Enterprise[i] == '-':
            Climate_Index_Enterprise[i] = np.NAN
        else:
            Climate_Index_Enterprise[i] = float(Climate_Index_Enterprise[i])
        if Macro_econ_Climate_Index[i] == '-':
            Macro_econ_Climate_Index[i] = np.NAN
        else:
            Macro_econ_Climate_Index[i] = float(Macro_econ_Climate_Index[i])

    Quarter.reverse()
    Climate_Index_Enterprise.reverse()
    Macro_econ_Climate_Index.reverse()

    plt.plot(Quarter[24:], Climate_Index_Enterprise[24:], c='Salmon', marker='.', label="企业景气指数")
    plt.plot(Quarter[24:], Macro_econ_Climate_Index[24:], c='SkyBlue', marker='.', label="企业家信心指数")
    plt.legend(loc='best')
    plt.ylim(50, 150)

    plt.text('2020年第1季度', 88.22 - 5, 88.22, ha='left', va='bottom', fontsize=24, color='Salmon', family='SimHei')
    plt.text('2020年第1季度', 88.22, '·', ha='center', va='center', fontsize=20, color='Salmon')
    plt.text('2020年第1季度', 90.86, '·', ha='center', va='center', fontsize=20, color='SkyBlue')
    plt.text('2020年第1季度', 90.86 + 2, 90.86, ha='left', va='bottom', fontsize=24, color='SkyBlue', family='SimHei')

    plt.text('2019年第4季度', 145, '2019年第4季度', ha='center', va='center', fontsize=20, color='darkred', family='SimHei')
    plt.vlines('2019年第4季度', 145, 0.5, colors="darkred", linestyles="dashed")

    plt.gca().xaxis.set_major_locator(ticker.MultipleLocator(6))
    plt.xlabel("年份", fontdict={'size': 16})
    plt.ylabel("数据", fontdict={'size': 16})
    plt.title("Enterprise_Confidence", fontdict={'size': 20})
    plt.xticks(size=20)
    plt.yticks(size=20)

    ax = plt.gca();  # 获得坐标轴的句柄
    ax.spines['bottom'].set_linewidth(2);  ###设置底部坐标轴的粗细
    ax.spines['left'].set_linewidth(2);  ####设置左边坐标轴的粗细
    ax.spines['right'].set_linewidth(2);  ###设置右边坐标轴的粗细
    ax.spines['top'].set_linewidth(2);  ####设置上部坐标轴的粗细
    plt.savefig('pic/Enterprise_Confidence.png')
    plt.show()


pmi()
cpi()
cci()
Fiscal_Revenue()
National_Tax_Revenue()
gdp()
Gas_Price()
Enterprise_Confidence()
