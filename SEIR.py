import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from mpl_toolkits.axisartist.parasite_axes import HostAxes, ParasiteAxes

plt.rcParams['font.family'] = 'SimHei'
plt.rcParams["axes.unicode_minus"] = False


def dySEIDR_V2(y, t, alpha, beta0, beta1, beta2, gamma0, gamma1, gamma2, delta0, delta1, delta2, lamda, v1, v2):
    s0, s1, s2, e0, e1, e2, i0, i1, i2, d0, d1, d2, r = y
    n = s0 + s1 + s2 + e0 + e1 + e2 + i0 + i1 + i2 + d0 + d1 + d2 + r

    i_e = i0 + i1 + i2 + e0 + e1 + e2

    ds0_dt = - lamda * beta0 * s0 * i_e / n - v1 * s0
    ds1_dt = - lamda * beta1 * s1 * i_e / n + v1 * s0 - v2 * s1
    ds2_dt = - lamda * beta2 * s2 * i_e / n + v2 * s1
    de0_dt = lamda * beta0 * s0 * i_e / n - alpha * e0
    de1_dt = lamda * beta1 * s1 * i_e / n - alpha * e1
    de2_dt = lamda * beta2 * s2 * i_e / n - alpha * e2
    di0_dt = alpha * e0 - gamma0 * i0 - delta0 * i0
    di1_dt = alpha * e1 - gamma1 * i1 - delta1 * i1
    di2_dt = alpha * e2 - gamma2 * i2 - delta2 * i2
    dd0_dt = delta0 * i0
    dd1_dt = delta1 * i1
    dd2_dt = delta2 * i2
    dr_dt = gamma0 * i0 + gamma1 * i1 + gamma2 * i2

    return np.array([ds0_dt, ds1_dt, ds2_dt, de0_dt, de1_dt, de2_dt, di0_dt, di1_dt, di2_dt, dd0_dt, dd1_dt, dd2_dt, dr_dt])


def draw_SEIDR(ySEIR):
    fig = plt.figure(1)
    ax = HostAxes(fig, [0.1, 0.1, 0.7, 0.8])
    para1 = ParasiteAxes(ax, sharex=ax)
    para2 = ParasiteAxes(ax, sharex=ax)
    para3 = ParasiteAxes(ax, sharex=ax)
    para4 = ParasiteAxes(ax, sharex=ax)
    ax.parasites.append(para1)
    ax.parasites.append(para2)
    ax.parasites.append(para3)
    ax.parasites.append(para4)
    ax.axis['right'].set_visible(False)
    ax.axis['top'].set_visible(False)
    para1.axis['right'].set_visible(True)
    para1.axis['right'].major_ticklabels.set_visible(True)
    para1.axis['right'].label.set_visible(True)
    ax.set_ylabel('易感人数')
    ax.set_xlabel('时间/天')
    # para1.set_ylabel('潜伏人数')
    # para2.set_ylabel('患病人数')
    # para3.set_ylabel('死亡人数')
    # para4.set_ylabel('康复人数')
    para2_axis = para2.get_grid_helper().new_fixed_axis
    para3_axis = para3.get_grid_helper().new_fixed_axis
    para4_axis = para4.get_grid_helper().new_fixed_axis
    para2.axis['right2'] = para2_axis(loc='right', axes=para2, offset=(15, 0))
    para3.axis['right3'] = para3_axis(loc='right', axes=para3, offset=(30, 0))
    para4.axis['right4'] = para4_axis(loc='right', axes=para4, offset=(45, 0))
    fig.add_axes(ax)
    ax.plot(t, ySEIR[:, 0] + ySEIR[:, 1] + ySEIR[:, 2], '--', label='易感人数', color='black')
    para1.plot(t, ySEIR[:, 3] + ySEIR[:, 4] + ySEIR[:, 5], '-.', label='潜伏人数', color='red')
    para2.plot(t, ySEIR[:, 6] + ySEIR[:, 7] + ySEIR[:, 8], '-', label='患病人数', color='green')
    para3.plot(t, ySEIR[:, 9] + ySEIR[:, 10] + ySEIR[:, 11], '.', label='死亡人数', color='purple')
    para4.plot(t, ySEIR[:, 12], '--', label='康复人数', color='blue')
    ax.set_ylim(0, 2.7e9)
    # 轴名称，刻度值的颜色
    para1.axis['right'].label.set_color('red')
    para2.axis['right2'].label.set_color('green')
    para3.axis['right3'].label.set_color('purple')
    para4.axis['right4'].label.set_color('blue')
    para1.axis['right'].major_ticks.set_color('red')
    para2.axis['right2'].major_ticks.set_color('green')
    para3.axis['right3'].major_ticks.set_color('purple')
    para4.axis['right4'].major_ticks.set_color('blue')
    para1.axis['right'].major_ticklabels.set_color('red')
    para2.axis['right2'].major_ticklabels.set_color('green')
    para3.axis['right3'].major_ticklabels.set_color('purple')
    para4.axis['right4'].major_ticklabels.set_color('blue')
    para1.axis['right'].line.set_color('red')
    para2.axis['right2'].line.set_color('green')
    para3.axis['right3'].line.set_color('purple')
    para4.axis['right4'].line.set_color('blue')
    ax.legend(loc='right')
    plt.title('SEIR模型预测')
    plt.show()


if __name__ == '__main__':
    number = 1.4e10      # 模型总人数

    s = 1395999707            # 易感人群数量
    e = 1262               # 暴露者/潜伏者
    i = 87          # 感染者
    d = 20274            # 死亡者
    r = 296678            # 康复者

    alpha = 0.05        # 潜伏期的人变成感染者的概率
    beta = 0.05     # 对于易感者，与感染者接触后成为潜伏者的可能性
    gamma = 0.07        # 感染者的治愈率
    delta = 0.005    # 感染者的死亡率
    lamda = 2           # 单位时间内受感染者接触的易受感染人数

    tEnd = 300          # 300天
    t = np.arange(0, tEnd, 1)

    v1 = 0.9            # 第一针疫苗接种率
    v2 = 0.87            # 第二针疫苗接种率
    beta0 = 0.05        # 未打疫苗人群的患病概率
    beta1 = 0.01        # 已打疫苗人群的感染率
    beta2 = 0.005       # 已打疫苗人群的感染率
    gamma0 = 0.08       # 未接种疫苗的感染者的治愈率
    gamma1 = 0.10       # 接种了疫苗的感染者的治愈率
    gamma2 = 0.10       # 接种了疫苗的感染者的治愈率
    delta0 = 0.02       # 未接种疫苗的感染者的死亡率
    delta1 = 0.001      # 接种了疫苗的感染者的死亡率
    delta2 = 0.0008     # 接种了疫苗的感染者的死亡率
    s0 = 192587000           # 未接种疫苗人群
    s1 = 1259967000              # 接种一针疫苗人群
    s2 = 1207413000              # 接种两针疫苗人群
    e0 = 0              # 未接种疫苗的潜伏人群
    e1 = 0              # 接种一针疫苗的潜伏人群
    e2 = 0              # 接种两针疫苗的潜伏人群
    i0 = 87        # 未接种疫苗的感染人群
    i1 = 0              # 接种一针疫苗的感染人群
    i2 = 0              # 接种两针疫苗的感染人群
    d0 = 0              # 未接种疫苗的死亡人群
    d1 = 0              # 接种一针疫苗的死亡人群
    d2 = 0              # 接种两针疫苗的感染人群

    Y0 = (s0, s1, s2, e0, e1, e2, i0, i1, i2, d0, d1, d2, r)
    ySEIR = odeint(dySEIDR_V2, Y0, t, args=(alpha, beta0, beta1, beta2, gamma0, gamma1, gamma2, delta0, delta1, delta2, lamda, v1, v2))
    draw_SEIDR(ySEIR)
