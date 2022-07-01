import pandas as pd
from typing import List, Union

from pyecharts import options as opts
from pyecharts.commons.utils import JsCode
from pyecharts.charts import Kline, Line, Bar, Grid

data = pd.read_csv(r'数据/道琼斯工业平均数.csv')
list_name = ['TRV', 'WBA', 'JPM', 'CSCO', 'MSFT', 'DIS', 'PG', 'BA', 'KO', 'MMM', 'INTC', 'JNJ', 'IBM', 'HD',
             'CVX', 'GS', 'HON', 'MRK', 'CAT', 'AXP', 'NKE', 'UNH', 'WMT', 'MCD', 'VZ', 'AMGN']
data1 = data.loc[data['stock'] == 'AAPL']
for name in list_name:
    data_ = data.loc[data['stock'] == name]
    data1['open_'] = list(data_['open'])
    data1['open'] = (data1['open'] + data1['open_']) / ([2] * len(data1))
    data1['high_'] = list(data_['high'])
    data1['high'] = (data1['high'] + data1['high_']) / ([2] * len(data1))
    data1['low_'] = list(data_['low'])
    data1['low'] = (data1['low'] + data1['low_']) / ([2] * len(data1))
    data1['close_'] = list(data_['close'])
    data1['close'] = (data1['close'] + data1['close_']) / ([2] * len(data1))
    data1['volume_'] = list(data_['volume'])
    data1['volume'] = (data1['volume'] + data1['volume_']) / ([2] * len(data1))
data1 = data1.drop(['stock', 'adj_close', 'dividend', 'split', 'open_', 'high_', 'low_', 'close_', 'volume_'], axis=1)
data1['open'] = data1['open'].astype(int)
data1['high'] = data1['high'].astype(int)
data1['low'] = data1['low'].astype(int)
data1['close'] = data1['close'].astype(int)
data1['volume'] = data1['volume'].astype(int)
print(data1)
echarts_data = data1.values.tolist()


def split_data(origin_data) -> dict:
    datas = []
    times = []
    vols = []

    for i in range(len(origin_data)):
        datas.append(origin_data[i][1:])
        times.append(origin_data[i][0:1][0])
        vols.append(origin_data[i][5])
    vols = [int(v) for v in vols]

    return {
        "datas": datas,
        "times": times,
        "vols": vols,
    }


def calculate_ma(day_count: int):
    result: List[Union[float, str]] = []

    for i in range(len(data["times"])):
        if i < day_count:
            result.append("-")
            continue
        sum_total = 0.0
        for j in range(day_count):
            sum_total += float(data["datas"][i - j][1])
        result.append(abs(float("%.2f" % (sum_total / day_count))))
    return result


def draw_chart():
    kline = (
        Kline()
        .add_xaxis(xaxis_data=data["times"])
        .add_yaxis(
            series_name="",
            y_axis=data["datas"],
            itemstyle_opts=opts.ItemStyleOpts(
                color="#ef232a",
                color0="#14b143",
                border_color="#ef232a",
                border_color0="#14b143",
            ),
            markpoint_opts=opts.MarkPointOpts(
                data=[
                    opts.MarkPointItem(type_="max", name="最大值"),
                    opts.MarkPointItem(type_="min", name="最小值"),
                ]
            ),

        )
        .set_global_opts(
            title_opts=opts.TitleOpts(title="K线周期图表", pos_left="0"),
            xaxis_opts=opts.AxisOpts(
                type_="category",
                is_scale=True,
                boundary_gap=False,
                axisline_opts=opts.AxisLineOpts(is_on_zero=False),
                splitline_opts=opts.SplitLineOpts(is_show=False),
                split_number=20,
                min_="dataMin",
                max_="dataMax",
            ),
            yaxis_opts=opts.AxisOpts(
                is_scale=True, splitline_opts=opts.SplitLineOpts(is_show=True)
            ),
            tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="line"),
            datazoom_opts=[
                opts.DataZoomOpts(
                    is_show=False, type_="inside", xaxis_index=[0, 0], range_end=100
                ),
                opts.DataZoomOpts(
                    is_show=True, xaxis_index=[0, 1], pos_top="97%", range_end=100
                ),
            ],
        )
    )
    kline_line = (
        Line()
        .add_xaxis(xaxis_data=data["times"])
        .add_yaxis(
            series_name="MA5",
            y_axis=calculate_ma(day_count=5),
            is_smooth=True,
            linestyle_opts=opts.LineStyleOpts(opacity=0.5),
            label_opts=opts.LabelOpts(is_show=False),
        )
        .set_global_opts(
            xaxis_opts=opts.AxisOpts(
                type_="category",
                grid_index=1,
                axislabel_opts=opts.LabelOpts(is_show=False),
            ),
            yaxis_opts=opts.AxisOpts(
                grid_index=1,
                split_number=3,
                axisline_opts=opts.AxisLineOpts(is_on_zero=False),
                axistick_opts=opts.AxisTickOpts(is_show=False),
                splitline_opts=opts.SplitLineOpts(is_show=False),
                axislabel_opts=opts.LabelOpts(is_show=True),
            ),
        )
    )
    overlap_kline_line = kline.overlap(kline_line)
    bar_1 = (
        Bar()
        .add_xaxis(xaxis_data=data["times"])
        .add_yaxis(
            series_name="Volumn",
            yaxis_data=data["vols"],
            xaxis_index=1,
            yaxis_index=1,
            label_opts=opts.LabelOpts(is_show=False),
            itemstyle_opts=opts.ItemStyleOpts(
                color=JsCode(
                    """
                function(params) {
                    var colorList;
                    if (barData[params.dataIndex][1] > barData[params.dataIndex][0]) {
                        colorList = '#ef232a';
                    } else {
                        colorList = '#14b143';
                    }
                    return colorList;
                }
                """
                )
            ),
        )
        .set_global_opts(
            xaxis_opts=opts.AxisOpts(
                type_="category",
                grid_index=1,
                axislabel_opts=opts.LabelOpts(is_show=False),
            ),
            legend_opts=opts.LegendOpts(is_show=False),
        )
    )
    grid_chart = Grid(init_opts=opts.InitOpts())

    # 这个是为了把 data.datas 这个数据写入到 html 中,还没想到怎么跨 series 传值
    # demo 中的代码也是用全局变量传的
    grid_chart.add_js_funcs("var barData = {}".format(data["datas"]))

    # K线图和 MA5 的折线图
    grid_chart.add(
        overlap_kline_line,
        grid_opts=opts.GridOpts(pos_left="3%", pos_right="1%", height="60%"),
    )
    # Volumn 柱状图
    grid_chart.add(
        bar_1,
        grid_opts=opts.GridOpts(
            pos_left="3%", pos_right="1%", pos_top="71%", height="10%"
        ),
    )
    grid_chart.render("professional_kline_chart.html")


if __name__ == "__main__":
    data = split_data(origin_data=echarts_data)
    draw_chart()
