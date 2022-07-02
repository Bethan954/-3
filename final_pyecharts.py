import pandas as pd
import numpy as np
import pyecharts.options as opts
from pyecharts.charts import *


def pmi():
    df_PMI = pd.read_csv("data/gmjj/PMI.csv")
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
    (
        Line(init_opts=opts.InitOpts(width="1600px", height="800px"))
            .add_xaxis(xaxis_data=month[120:])
            .add_yaxis(
            series_name="制造业同比增长",
            y_axis=Manufacturing_YOY[120:],
            markpoint_opts=opts.MarkPointOpts(
                data=[
                    opts.MarkPointItem(type_="max", name="最大值", symbol_size=86),
                    opts.MarkPointItem(type_="min", name="最小值", symbol_size=86),
                ]
            ),
            markline_opts=opts.MarkLineOpts(
                data=[opts.MarkLineItem(type_="average", name="平均值")]
            ),
            label_opts=opts.LabelOpts(is_show=False),
            linestyle_opts=opts.LineStyleOpts(width=3)
        )
            .add_yaxis(
            series_name="非制造业同比增长",
            y_axis=Nonmanufacturing_YOY[120:],
            markpoint_opts=opts.MarkPointOpts(

                data=[
                    opts.MarkPointItem(type_="max", name="最大值", symbol_size=86),
                    opts.MarkPointItem(type_="min", name="最小值", symbol_size=86),
                ]

            ),
            #         label_opts = opts.LabelOpts(position="inside", color="#fff", font_size=16),
            markline_opts=opts.MarkLineOpts(
                data=[opts.MarkLineItem(type_="average", name="平均值")]
            ),
            label_opts=opts.LabelOpts(is_show=False),
            linestyle_opts=opts.LineStyleOpts(width=3)
        )
            .set_global_opts(
            tooltip_opts=opts.TooltipOpts(trigger="axis"),
            toolbox_opts=opts.ToolboxOpts(is_show=True),
            xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(font_size=16  # 字的大小
                                                                   , font_weight='bolder')),
            yaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(font_size=16  # 字的大小
                                                                   , font_weight='bolder'),
                                     axistick_opts=opts.AxisTickOpts(is_show=True),
                                     splitline_opts=opts.SplitLineOpts(is_show=True))
        )
            .render('pmi.html')
    )


def cpi():
    df_cpi = pd.read_csv("data/gmjj/CPI.csv")  # 08-22年间，每月中国居民消费价格指数
    Month = df_cpi['Month'].tolist()
    Nation_Current_Month = df_cpi['Nation_Current_Month'].tolist()
    City_Current_Month = df_cpi['City_Current_Month'].tolist()
    Country_Current_Month = df_cpi['Country_Current_Month'].tolist()

    Month.reverse()
    Nation_Current_Month.reverse()
    City_Current_Month.reverse()
    Country_Current_Month.reverse()

    (
        Line(init_opts=opts.InitOpts(width="1600px", height="800px"))
            .add_xaxis(xaxis_data=Month[108:])
            .add_yaxis(
            series_name="全国",
            y_axis=Nation_Current_Month[108:],
            markpoint_opts=opts.MarkPointOpts(
                data=[
                    opts.MarkPointItem(type_="max", name="最大值", symbol_size=86),
                    opts.MarkPointItem(type_="min", name="最小值", symbol_size=86),
                ]
            ),
            markline_opts=opts.MarkLineOpts(
                data=[opts.MarkLineItem(type_="average", name="平均值")]
            ),
            label_opts=opts.LabelOpts(is_show=False),
            linestyle_opts=opts.LineStyleOpts(width=3)
        )
            .add_yaxis(
            series_name="城市",
            y_axis=City_Current_Month[108:],
            markpoint_opts=opts.MarkPointOpts(
                data=[
                    opts.MarkPointItem(type_="max", name="最大值", symbol_size=86),
                    opts.MarkPointItem(type_="min", name="最小值", symbol_size=86),
                ]
            ),
            markline_opts=opts.MarkLineOpts(
                data=[opts.MarkLineItem(type_="average", name="平均值")]
            ),
            label_opts=opts.LabelOpts(is_show=False),
            linestyle_opts=opts.LineStyleOpts(width=3)
        )
            .add_yaxis(
            series_name="农村",
            y_axis=Country_Current_Month[108:],
            markpoint_opts=opts.MarkPointOpts(
                data=[
                    opts.MarkPointItem(type_="max", name="最大值", symbol_size=86),
                    opts.MarkPointItem(type_="min", name="最小值", symbol_size=86),
                ]
            ),
            markline_opts=opts.MarkLineOpts(
                data=[opts.MarkLineItem(type_="average", name="平均值")]
            ),
            label_opts=opts.LabelOpts(is_show=False),
            linestyle_opts=opts.LineStyleOpts(width=3)
        )
            .set_global_opts(
            #         title_opts=opts.TitleOpts(title="CPI"),
            tooltip_opts=opts.TooltipOpts(trigger="axis"),
            toolbox_opts=opts.ToolboxOpts(is_show=True),
            #         xaxis_opts=opts.AxisOpts(type_="category", boundary_gap=False),
            xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(font_size=16  # 字的大小
                                                                   , font_weight='bolder')),
            yaxis_opts=opts.AxisOpts(
                axislabel_opts=opts.LabelOpts(font_size=16  # 字的大小
                                              , font_weight='bolder')
                , min_=98)
        )
            .render('cpi.html')
    )


def cci():
    df_cci = pd.read_csv("data/gmjj/CCI.csv")  # 07-21年间，中国消费者信心指数数据
    """
    指数值
    """
    Month = df_cci['Month'].tolist()
    CCI = df_cci['CCI'].tolist()
    CSI = df_cci['CSI'].tolist()
    CEI = df_cci['CEI'].tolist()

    Month.reverse()
    CCI.reverse()
    CSI.reverse()
    CEI.reverse()

    """
    同比增长
    """

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

    (
        Line(init_opts=opts.InitOpts(width="1600px", height="800px"))
            .add_xaxis(xaxis_data=Month[108:])
            .add_yaxis(
            series_name="消费者信心同比增长",
            y_axis=CCI_YOY[108:],
            markpoint_opts=opts.MarkPointOpts(
                data=[
                    opts.MarkPointItem(type_="max", name="最大值", symbol_size=72),
                    opts.MarkPointItem(type_="min", name="最小值", symbol_size=72),
                ]
            ),
            markline_opts=opts.MarkLineOpts(
                data=[opts.MarkLineItem(type_="average", name="平均值")]
            ),
            label_opts=opts.LabelOpts(is_show=False),
            linestyle_opts=opts.LineStyleOpts(width=3)
        )
            .add_yaxis(
            series_name="消费者满意同比增长",
            y_axis=CSI_YOY[108:],
            markpoint_opts=opts.MarkPointOpts(
                data=[
                    opts.MarkPointItem(type_="max", name="最大值", symbol_size=72),
                    opts.MarkPointItem(type_="min", name="最小值", symbol_size=72),
                ]
            ),
            markline_opts=opts.MarkLineOpts(
                data=[opts.MarkLineItem(type_="average", name="平均值")]
            ),
            label_opts=opts.LabelOpts(is_show=False),
            linestyle_opts=opts.LineStyleOpts(width=3)
        )
            .add_yaxis(
            series_name="消费者预期同比增长",
            y_axis=CEI_YOY[108:],
            markpoint_opts=opts.MarkPointOpts(
                data=[
                    opts.MarkPointItem(type_="max", name="最大值", symbol_size=72),
                    opts.MarkPointItem(type_="min", name="最小值", symbol_size=72),
                ]
            ),
            markline_opts=opts.MarkLineOpts(
                data=[opts.MarkLineItem(type_="average", name="平均值")]
            ),
            label_opts=opts.LabelOpts(is_show=False),
            linestyle_opts=opts.LineStyleOpts(width=3)
        )
            .set_global_opts(
            #         title_opts=opts.TitleOpts(title="CCI"),
            tooltip_opts=opts.TooltipOpts(trigger="axis"),
            toolbox_opts=opts.ToolboxOpts(is_show=True),
            xaxis_opts=opts.AxisOpts(type_="category", boundary_gap=False,
                                     axislabel_opts=opts.LabelOpts(font_size=16  # 字的大小
                                                                   , font_weight='bolder')),
            yaxis_opts=opts.AxisOpts(
                axislabel_opts=opts.LabelOpts(font_size=16  # 字的大小
                                              , font_weight='bolder'))
        )
            .render('cci.html')
    )


def fiscal_revenue():
    df_Fiscal_Revenue = pd.read_csv("data/gmjj/Fiscal_Revenue.csv")  # 08-21年间，每月中国财政收入数据
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

    bar = (
        Bar()
            .add_xaxis(Month[112:])
            .add_yaxis("当月收入（亿元）"
                       , Current_Month_Value[112:]
                       , label_opts=opts.LabelOpts(is_show=False))
            #               ,color='#2f4554')

            .extend_axis(
            yaxis=opts.AxisOpts(
                name="增长比率",
                type_="value",
                min_=-100,
                max_=45,
                position="right",
                axislabel_opts=opts.LabelOpts(formatter="{value} %"),
            )
        )
            .set_global_opts(
            #          title_opts=opts.TitleOpts(title="Fiscal_Revenue")
            datazoom_opts=opts.DataZoomOpts(is_show=True
                                            , range_start=0  # 显示区域的开始位置，默认是20
                                            , range_end=80  # 显示区域的结束位置，默认是80
                                            , orient='horizontal'  ##缩放区域空值条所放的位置
                                            )
        )
    )

    line = (
        Line(init_opts=opts.InitOpts(width="1600px", height="800px"))
            .add_xaxis(xaxis_data=Month[112:])
            .add_yaxis(
            series_name="同比增长",
            y_axis=Current_Month_YOY[112:],
            #         symbol='.',
            markpoint_opts=opts.MarkPointOpts(
                data=[
                    opts.MarkPointItem(type_="max", name="最大值", symbol_size=72),
                    opts.MarkPointItem(type_="min", name="最小值", symbol_size=72),
                ]
            ),
            markline_opts=opts.MarkLineOpts(
                data=[opts.MarkLineItem(type_="average", name="平均值")]
            ),
            label_opts=opts.LabelOpts(is_show=False)
            , yaxis_index=1
            , linestyle_opts=opts.LineStyleOpts(width=3)
        )
            .set_global_opts(
            #         title_opts=opts.TitleOpts(title="Fiscal_Revenue"),
            tooltip_opts=opts.TooltipOpts(trigger="axis"),
            toolbox_opts=opts.ToolboxOpts(is_show=True),
            xaxis_opts=opts.AxisOpts(type_="category", boundary_gap=False,
                                     axislabel_opts=opts.LabelOpts(font_size=16  # 字的大小
                                                                   , font_weight='bolder')),
            yaxis_opts=opts.AxisOpts(
                axislabel_opts=opts.LabelOpts(font_size=16  # 字的大小
                                              , font_weight='bolder'))

        )
        #     .render_notebook()
    )
    bar.overlap(line)  # 在柱状图上叠加折线图
    bar.render("fiscal_revenue.html")


def national_tax_revenue():
    df_National_Tax_Revenue = pd.read_csv("data/gmjj/National_Tax_Revenue.csv")  # 08-21年间，每月中国财政收入数据
    Quarter = df_National_Tax_Revenue['Quarter'].tolist()
    YOY = df_National_Tax_Revenue['YOY'].tolist()

    for i in range(len(YOY)):
        if YOY[i][-1] != '%':
            YOY[i] = np.NAN
        else:
            YOY[i] = float(YOY[i][:-1])

    Quarter.reverse()
    YOY.reverse()

    (
        Line(init_opts=opts.InitOpts(width="1600px", height="800px"))
            .add_xaxis(xaxis_data=Quarter)
            .add_yaxis(
            series_name="较上年同期(%)",
            y_axis=YOY,
            markpoint_opts=opts.MarkPointOpts(
                data=[
                    opts.MarkPointItem(type_="max", name="最大值", symbol_size=72),
                    opts.MarkPointItem(type_="min", name="最小值", symbol_size=72),
                ]
            ),
            markline_opts=opts.MarkLineOpts(
                data=[opts.MarkLineItem(type_="average", name="平均值")]
            ),
            label_opts=opts.LabelOpts(is_show=False)
            , linestyle_opts=opts.LineStyleOpts(width=3)
        )

            .set_global_opts(
            #         title_opts=opts.TitleOpts(title="National_Tax_Revenue"),
            tooltip_opts=opts.TooltipOpts(trigger="axis"),
            toolbox_opts=opts.ToolboxOpts(is_show=True),
            xaxis_opts=opts.AxisOpts(type_="category", boundary_gap=False,
                                     axislabel_opts=opts.LabelOpts(font_size=16  # 字的大小
                                                                   , font_weight='bolder')),
            yaxis_opts=opts.AxisOpts(
                axislabel_opts=opts.LabelOpts(font_size=16  # 字的大小
                                              , font_weight='bolder'))

        )
            .render('national_tax_revenue.html')
    )


def gdp():
    df_GDP = pd.read_csv("data/gmjj/GDP.csv")  # 08-20年间，每月中国外商直接投资数据
    Quater = df_GDP['Quater'].tolist()
    GDP_YOY = df_GDP['GDP_YOY'].tolist()
    Primary_Indusry_YOY = df_GDP['Primary_Indusry_YOY'].tolist()
    Secondary_Indusry_YOY = df_GDP['Secondary_Indusry_YOY'].tolist()
    Tertiary_Indusry_YOY = df_GDP['Tertiary_Indusry_YOY'].tolist()

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

    (
        Line(init_opts=opts.InitOpts(width="1600px", height="800px"))
            .add_xaxis(xaxis_data=Quater[48:])
            .add_yaxis(
            series_name="国内生产总值同比增长",
            y_axis=GDP_YOY[48:],
            markpoint_opts=opts.MarkPointOpts(
                data=[
                    opts.MarkPointItem(type_="max", name="最大值", symbol_size=72),
                    opts.MarkPointItem(type_="min", name="最小值", symbol_size=72),
                ]
            ),
            markline_opts=opts.MarkLineOpts(
                data=[opts.MarkLineItem(type_="average", name="平均值")]
            ),
            label_opts=opts.LabelOpts(is_show=False)
            , linestyle_opts=opts.LineStyleOpts(width=3)
        )
            .add_yaxis(
            series_name="第一产业同比增长",
            y_axis=Primary_Indusry_YOY[48:],
            markpoint_opts=opts.MarkPointOpts(
                data=[
                    opts.MarkPointItem(type_="max", name="最大值", symbol_size=72),
                    opts.MarkPointItem(type_="min", name="最小值", symbol_size=72),
                ]
            ),
            markline_opts=opts.MarkLineOpts(
                data=[opts.MarkLineItem(type_="average", name="平均值")]
            ),
            label_opts=opts.LabelOpts(is_show=False)
            , linestyle_opts=opts.LineStyleOpts(width=3)
        )
            .add_yaxis(
            series_name="第二产业同比增长",
            y_axis=Secondary_Indusry_YOY[48:],
            markpoint_opts=opts.MarkPointOpts(
                data=[
                    opts.MarkPointItem(type_="max", name="最大值", symbol_size=72),
                    opts.MarkPointItem(type_="min", name="最小值", symbol_size=72),
                ]
            ),
            markline_opts=opts.MarkLineOpts(
                data=[opts.MarkLineItem(type_="average", name="平均值")]
            ),
            label_opts=opts.LabelOpts(is_show=False)
            , linestyle_opts=opts.LineStyleOpts(width=3)
        )
            .add_yaxis(
            series_name="第三产业同比增长",
            y_axis=Tertiary_Indusry_YOY[48:],
            markpoint_opts=opts.MarkPointOpts(
                data=[
                    opts.MarkPointItem(type_="max", name="最大值", symbol_size=72),
                    opts.MarkPointItem(type_="min", name="最小值", symbol_size=72),
                ]
            ),
            markline_opts=opts.MarkLineOpts(
                data=[opts.MarkLineItem(type_="average", name="平均值")]
            ),
            label_opts=opts.LabelOpts(is_show=False)
            , linestyle_opts=opts.LineStyleOpts(width=3)
        )
            .set_global_opts(
            #         title_opts=opts.TitleOpts(title="GDP"),
            tooltip_opts=opts.TooltipOpts(trigger="axis"),
            toolbox_opts=opts.ToolboxOpts(is_show=True),
            xaxis_opts=opts.AxisOpts(type_="category", boundary_gap=False,
                                     axislabel_opts=opts.LabelOpts(font_size=16  # 字的大小
                                                                   , font_weight='bolder')),
            yaxis_opts=opts.AxisOpts(
                axislabel_opts=opts.LabelOpts(font_size=16  # 字的大小
                                              , font_weight='bolder'))

        )
            .render('gdp.html')
    )


def enterprise_confidence():
    df_Enterprise_Confidence = pd.read_csv("data/gmjj/Enterprise_Confidence.csv")  # 00-22年间，中国油价调整数据
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

    (
        Line(init_opts=opts.InitOpts(width="1600px", height="800px"))
            .add_xaxis(xaxis_data=Quarter[36:])
            .add_yaxis(
            series_name="企业景气指数",
            y_axis=Climate_Index_Enterprise[36:],
            markpoint_opts=opts.MarkPointOpts(
                data=[
                    opts.MarkPointItem(type_="max", name="最大值", symbol_size=72),
                    opts.MarkPointItem(type_="min", name="最小值", symbol_size=72),
                ]
            ),
            markline_opts=opts.MarkLineOpts(
                data=[opts.MarkLineItem(type_="average", name="平均值")]
            ),
            label_opts=opts.LabelOpts(is_show=False)
            , linestyle_opts=opts.LineStyleOpts(width=3)
        )
            .add_yaxis(
            series_name="企业家信心指数",
            y_axis=Macro_econ_Climate_Index[36:],
            markpoint_opts=opts.MarkPointOpts(
                data=[
                    opts.MarkPointItem(type_="max", name="最大值", symbol_size=72),
                    opts.MarkPointItem(type_="min", name="最小值", symbol_size=72),
                ]
            ),
            markline_opts=opts.MarkLineOpts(
                data=[opts.MarkLineItem(type_="average", name="平均值")]
            ),
            label_opts=opts.LabelOpts(is_show=False)
            , linestyle_opts=opts.LineStyleOpts(width=3)
        )
            .set_global_opts(
            #         title_opts=opts.TitleOpts(title="Enterprise_Confidence"),
            tooltip_opts=opts.TooltipOpts(trigger="axis"),
            toolbox_opts=opts.ToolboxOpts(is_show=True),
            xaxis_opts=opts.AxisOpts(type_="category", boundary_gap=False,
                                     axislabel_opts=opts.LabelOpts(font_size=16  # 字的大小
                                                                   , font_weight='bolder')),
            yaxis_opts=opts.AxisOpts(
                axislabel_opts=opts.LabelOpts(font_size=16  # 字的大小
                                              , font_weight='bolder'),
                min_=80
            )
        )
        .render('enterprise_confidence.html')
    )


def unemployment_rate():
    df = pd.read_csv("data/WEOOct2021all.csv")
    df1 = df.loc[df['Subject Descriptor'] == 'Unemployment rate']
    Country = ['Australia', 'Canada', 'Colombia', 'France', 'Germany', 'Italy', 'Japan', 'Korea', 'Singapore',
               'Taiwan Province of China', 'Hong Kong SAR', 'China', 'United Kingdom', 'United States']
    df1 = df1.loc[df1['Country'].isin(Country)]
    df1 = df1.drop(columns=['WEO Country Code', 'ISO', 'WEO Subject Code', 'Subject Notes', 'Units', 'Scale',
                            'Country/Series-specific Notes'])
    df1 = df1.dropna()
    df1 = df1.reset_index(drop=True)

    df2 = df1.T
    df2.columns = list(range(0, 14, 1))

    year = list(df2.index)[2:-1]
    country = df1['Country'].tolist()
    data = []
    all_data = []
    for i in range(14):
        for j in df2[i].tolist()[2:-1]:
            data.append(float(j))
        all_data.append(data)
        data = []
    # all_data

    import matplotlib as mpl
    import matplotlib.pyplot as plt
    import matplotlib.ticker as ticker
    from matplotlib import colors
    mpl.rc("font", family='YouYuan')
    plt.figure(figsize=(20, 10), dpi=100)

    color = ['#EEE8AA',
             '#D8BFD8',
             '#AFEEEE',
             '#DB7093',
             '#F08080',
             '#FFDAB9',
             '#CD853F',
             '#FFC0CB',
             '#DDA0DD',
             '#B0E0E6',
             '#FFC0CB',
             '#9370DB',
             '#EE82EE',
             '#BC8F8F']
    year = list(df2.index)[2:-1]
    country = df1['Country'].tolist()
    data = []
    for i in range(14):
        for j in df2[i].tolist()[2:-1]:
            data.append(float(j))
        plt.plot(year, data, c=color[i], marker='.', label=country[i])
        #     print(color[i+108])
        data = []
    plt.legend(loc='best')
    plt.ylim(0, 30)

    plt.text('2020', 16.067, '16.067%', ha='left', va='bottom', fontsize=24, color='#DB7093', family='SimHei')
    plt.text('2020', 16.067, '·', ha='center', va='center', fontsize=20, color='#DB7093')
    plt.text('2020', 9.6, '9.6%', ha='left', va='bottom', fontsize=24, color='#D8BFD8', family='SimHei')
    plt.text('2020', 9.6, '·', ha='center', va='center', fontsize=20, color='#D8BFD8')
    plt.text('2020', 8.108, '8.108%', ha='left', va='bottom', fontsize=24, color='#BC8F8F', family='SimHei')
    plt.text('2020', 8.108, '·', ha='center', va='center', fontsize=20, color='#BC8F8F')

    plt.gca().xaxis.set_major_locator(ticker.MultipleLocator(3))
    plt.xlabel("年份", fontdict={'size': 16})
    plt.ylabel("数据", fontdict={'size': 16})
    plt.title("Unemployment Rate", fontdict={'size': 20})
    plt.xticks(size=20)
    plt.yticks(size=20)

    ax = plt.gca();  # 获得坐标轴的句柄
    ax.spines['bottom'].set_linewidth(2);  ###设置底部坐标轴的粗细
    ax.spines['left'].set_linewidth(2);  ####设置左边坐标轴的粗细
    ax.spines['right'].set_linewidth(2);  ###设置右边坐标轴的粗细
    ax.spines['top'].set_linewidth(2);  ####设置上部坐标轴的粗细
    plt.savefig('pic/Unemployment Rate.png')
    plt.show()


def global_gdp():
    df = pd.read_csv("data/WEOOct2021all.csv")
    # df.columns
    df1 = df.loc[df['WEO Subject Code'] == 'NGDPD']
    ISO = ['ITA', 'URY', 'CAN', 'AUS', 'KOR', 'ESP', 'ARG', 'MLT', 'PRT', 'ARE']
    df1 = df1.loc[df1['ISO'].isin(ISO)]
    df1 = df1.drop(columns=['WEO Country Code', 'Country',
                            'Subject Descriptor', 'Subject Notes', 'Units', 'Scale',
                            'Country/Series-specific Notes', '1980', '1981', '1982', '1983', '1984',
                            '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993',
                            '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002',
                            '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011',
                            '2012', '2013', '2014', '2015', '2016', '2017', 'Estimates Start After'])
    df1 = df1.dropna()
    df1 = df1.reset_index(drop=True)

    df2 = df1.T
    df2.columns = list(range(0, 10, 1))

    year = list(df2.index)[2:]
    ISO = df1['ISO'].tolist()
    data = []
    all_data = []
    for i in range(9):
        for j in df2[i].tolist()[2:]:
            data.append(float(j.replace(',', '')))
        all_data.append(data)
        data = []
    # all_data
    # year

    from pyecharts import options as opts
    from pyecharts.charts import *

    bar = (
        Bar()
            .add_xaxis(year)
            .add_yaxis("ARG", all_data[0])  # y轴设置
            .add_yaxis("AUS", all_data[1])  # y轴设置
            .add_yaxis("CAN", all_data[2])  # y轴设置
            .add_yaxis("ITA", all_data[3])  # y轴设置
            .add_yaxis("KOR", all_data[4])  # y轴设置
            .add_yaxis("MLT", all_data[5])  # y轴设置
            .add_yaxis("PRT", all_data[6])  # y轴设置
            .add_yaxis("ESP", all_data[7])  # y轴设置
            .add_yaxis("ARE", all_data[8])  # y轴设置
            .add_yaxis("URY", all_data[8])  # y轴设置
            #     .set_global_opts(title_opts=opts.TitleOpts(title="Bar-基本示例", subtitle="我是副标题"))
            .set_global_opts(title_opts=opts.TitleOpts(title="全球GDP情况")
                             , datazoom_opts=opts.DataZoomOpts(is_show=True
                                                               , range_start=0  # 显示区域的开始位置，默认是20
                                                               , range_end=80  # 显示区域的结束位置，默认是80
                                                               , orient='horizontal'  ##缩放区域空值条所放的位置
                                                               ),
                             xaxis_opts=opts.AxisOpts(
                                 axislabel_opts=opts.LabelOpts(font_size=16  # 字的大小
                                                               , font_weight='bolder')),
                             yaxis_opts=opts.AxisOpts(
                                 axislabel_opts=opts.LabelOpts(font_size=16  # 字的大小
                                                               , font_weight='bolder')
                             )
                             )

    )

    bar.render('global_gdp.html')


def yimiao():
    df = pd.read_csv("data/owid-covid-data.csv")
    cols = ['iso_code', 'date', 'total_vaccinations_per_hundred', 'people_vaccinated_per_hundred',
            'people_fully_vaccinated_per_hundred', 'total_boosters_per_hundred',
            'new_vaccinations_smoothed_per_million']
    df1 = df.loc[:, cols]
    # df1.info()
    df1 = df1.loc[df1['date'].isin(['2022-03-10'])]
    df1.dropna(inplace=True)

    df1 = df1.sort_values(by=['people_vaccinated_per_hundred'])
    df1.reset_index(inplace=True, drop=True)
    # df1

    iso_code = df1['iso_code'].tolist()[-10:]
    people_vaccinated_per_hundred = df1['people_vaccinated_per_hundred'].tolist()[-10:]
    x_data = iso_code
    y_data = people_vaccinated_per_hundred
    data_pair = [list(z) for z in zip(x_data, y_data)]
    data_pair.sort(key=lambda x: x[1])

    (
        Pie(init_opts=opts.InitOpts(width="1600px", height="800px"))
            .add(
            series_name="访问来源",
            data_pair=data_pair,
            rosetype="radius",
            #         radius="55%",
            #         center=["50%", "50%"],
            label_opts=opts.LabelOpts(is_show=False, position="center"),
        )
            .set_global_opts(
            title_opts=opts.TitleOpts(
                title="每100人中至少接种一剂的人数",
                pos_left="center",
                pos_top="20",
            ),
            legend_opts=opts.LegendOpts(is_show=False),
        )
            .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}% ({d}%)"))

            .render("yimiao.html")
    )

pmi()
cpi()
cci()
fiscal_revenue()
national_tax_revenue()
gdp()
enterprise_confidence()
unemployment_rate()
global_gdp()
yimiao()

