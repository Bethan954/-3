import pandas as pd
import pyecharts.options as opts
from pyecharts.charts import Line, Grid

data = pd.read_csv(r'数据/全球新冠肺炎疫情量化数据.csv')
data = data.loc[data['location'] == 'China']
data = data[['date', 'new_cases', 'reproduction_rate', 'stringency_index']]
data['new_cases'] = data['new_cases'].fillna(0)
data['stringency_index'] = data['stringency_index'].fillna(method='ffill')
print(data)
timeData = list(data['date'])
new_casesData = list(data['new_cases'])
stringency_indexData = list(data['stringency_index'])
reproduction_rateData = list(data['reproduction_rate'])


l1 = (
    Line()
    .add_xaxis(xaxis_data=timeData)
    .add_yaxis(
        series_name="新增人数",
        y_axis=new_casesData,
        symbol_size=8,
        is_hover_animation=False,
        label_opts=opts.LabelOpts(is_show=False),
        linestyle_opts=opts.LineStyleOpts(width=1.5),
        is_smooth=True,
        yaxis_index=0,
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(
            title="政策响应对每日新增及R的影响", pos_left="center"
        ),
        tooltip_opts=opts.TooltipOpts(trigger="axis"),
        axispointer_opts=opts.AxisPointerOpts(
            is_show=True, link=[{"xAxisIndex": "all"}]
        ),
        datazoom_opts=[
            opts.DataZoomOpts(
                is_show=True,
                is_realtime=True,
                start_value=30,
                end_value=70,
                xaxis_index=[0, 1, 2],
            ),
        ],
        xaxis_opts=opts.AxisOpts(
            type_="category",
            boundary_gap=False,
            axisline_opts=opts.AxisLineOpts(is_on_zero=True),
        ),
        yaxis_opts=opts.AxisOpts(name="新增人数(人/天)"),
        legend_opts=opts.LegendOpts(pos_left="left"),
        toolbox_opts=opts.ToolboxOpts(
            is_show=True,
            feature={
                "dataZoom": {"yAxisIndex": "none"},
                "restore": {},
                "saveAsImage": {},
            },
        ),
    )
)

l1_ = (
    Line()
    .add_xaxis(xaxis_data=timeData)
    .add_yaxis(
        series_name='R',
        y_axis=reproduction_rateData,
        symbol_size=8,
        is_hover_animation=False,
        label_opts=opts.LabelOpts(is_show=False),
        linestyle_opts=opts.LineStyleOpts(width=1.5),
        is_smooth=True,
    )
    .set_global_opts(
        axispointer_opts=opts.AxisPointerOpts(
            is_show=True, link=[{"xAxisIndex": "all"}]
        ),
        tooltip_opts=opts.TooltipOpts(trigger="axis"),
        xaxis_opts=opts.AxisOpts(
            grid_index=1,
            type_="category",
            boundary_gap=False,
            axisline_opts=opts.AxisLineOpts(is_on_zero=True),
        ),
        datazoom_opts=[
            opts.DataZoomOpts(
                is_realtime=True,
                type_="inside",
                start_value=30,
                end_value=70,
                xaxis_index=[0, 1, 2],
            )
        ],
        yaxis_opts=opts.AxisOpts(is_inverse=False, name="R", position="right"),
        legend_opts=opts.LegendOpts(pos_left="9%"),
    )
)

l2 = (
    Line()
    .add_xaxis(xaxis_data=timeData)
    .add_yaxis(
        series_name="政策回应",
        y_axis=stringency_indexData,
        xaxis_index=1,
        yaxis_index=2,
        symbol_size=8,
        is_hover_animation=False,
        label_opts=opts.LabelOpts(is_show=False),
        linestyle_opts=opts.LineStyleOpts(width=1.5),
        is_smooth=True,
    )
    .set_global_opts(
        axispointer_opts=opts.AxisPointerOpts(
            is_show=True, link=[{"xAxisIndex": "all"}]
        ),
        tooltip_opts=opts.TooltipOpts(trigger="axis"),
        xaxis_opts=opts.AxisOpts(
            grid_index=1,
            type_="category",
            boundary_gap=False,
            axisline_opts=opts.AxisLineOpts(is_on_zero=True, linestyle_opts=opts.LineStyleOpts(color='black')),
            position="top",
        ),
        datazoom_opts=[
            opts.DataZoomOpts(
                is_realtime=True,
                type_="inside",
                start_value=30,
                end_value=70,
                xaxis_index=[0, 1, 2],
            )
        ],
        yaxis_opts=opts.AxisOpts(is_inverse=True, name="政策回应"),
        legend_opts=opts.LegendOpts(pos_left="14%"),
    )
)

(
    Grid(init_opts=opts.InitOpts(width="1024px", height="768px"))
    .add(chart=l1, grid_opts=opts.GridOpts(pos_left=50, pos_right=50, height="35%"))
    .add(chart=l1_, grid_opts=opts.GridOpts(pos_left=50, pos_right=50, height="35%"))
    .add(chart=l2,grid_opts=opts.GridOpts(pos_left=50, pos_right=50, pos_top="55%", height="35%"),)
    .render("rainfall_and_water_flow.html")
)
