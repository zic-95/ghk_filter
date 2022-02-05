import re
import pandas as ps
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter


def g_filter(data, x0, g):
    x_est = x0
    retVal = []

    for msr in data:
        residual = msr - x_est
        x_est = x_est + g * residual
        retVal.append(x_est)

    return retVal


def gh_filter(data, x0, dx0, g, h, dt):
    x_est = x0
    dx = dx0
    retVal = []

    for msr in data:

        x_pred = x_est + (dx * dt)

        residual = msr - x_pred
        dx = dx + h * (residual / dt)
        x_est = x_pred + g * (residual)
        retVal.append(x_est)

    return retVal


if __name__ == "__main__":

    # get data
    file_loc = "lib/ghk_filter/python_scripts/thrusters_m1.xls"
    g = 9.81

    dat1 = ps.read_excel(file_loc, usecols="B:F")
    x_axis_1 = dat1.iloc[1:1203, 0].to_numpy(dtype=float)
    [float(i) for i in x_axis_1]
    raw_data_1 = dat1.iloc[1:1203, 1].to_numpy(dtype=float) * g

    dat2 = ps.read_excel(file_loc, usecols="E:F")
    x_axis_2 = np.arange(start=0, stop=10.86, step=0.01, dtype=float)
    raw_data_2 = dat2.iloc[1:1087, 1].to_numpy(dtype=float) * g

    # filter data
    ret_g_Val = g_filter(data=raw_data_2, x0=10, g=0.1)
    ret_gh_Val = gh_filter(data=raw_data_1, x0=0, dx0=0.05,
                           dt=0.01, g=0.5, h=0.01)

    # # plot data
    # polyDegg = 2
    # raw_data_2_COFF = np.polyfit(x_axis_2, raw_data_2, polyDegg)
    # raw_data_2_POLY = np.poly1d(raw_data_2_COFF)
    # raw_data_2_NEW = raw_data_2_POLY(x_axis_2)

    # ret_g_Val_COFF = np.polyfit(x_axis_2, ret_g_Val, polyDegg)
    # ret_g_Val_POLY = np.poly1d(ret_g_Val_COFF)
    # ret_g_Val_NEW = ret_g_Val_POLY(x_axis_2)

    # raw_data_1_COFF = np.polyfit(x_axis_1, raw_data_1, polyDegg)
    # raw_data_1_POLY = np.poly1d(raw_data_1_COFF)
    # raw_data_1_NEW = raw_data_1_POLY(x_axis_1)

    # ret_gh_Val_COFF = np.polyfit(x_axis_1, ret_gh_Val, polyDegg)
    # ret_gh_Val_POLY = np.poly1d(ret_gh_Val_COFF)
    # ret_gh_Val_NEW = ret_gh_Val_POLY(x_axis_1)

    markerSpacing = 25
    ax1 = plt.subplot(121)
    ax1.plot(x_axis_2, raw_data_2, '1',
             markevery=markerSpacing, c='xkcd:red')
    ax1.plot(x_axis_2, raw_data_2, '-', markevery=markerSpacing,
             label="raw data", c='xkcd:red')
    ax1.plot(x_axis_2, ret_g_Val,  '2',
             markevery=markerSpacing, c='xkcd:blue')
    ax1.plot(x_axis_2, ret_g_Val,  '-', markevery=markerSpacing,
             label="g_filter", c='xkcd:blue')

    ax1.set_xlabel('PWM [ms]', fontsize=18)
    ax1.set_ylabel('Thrust [N]', fontsize=18)
    ax1.set_title('PWM/Thrust', fontsize=25)
    ax1.legend(loc="upper left", fontsize=15)
    #ax1.set_xlim(1000, 1650)
    ax1.set_ylim(5, 15)
    ax1.grid(True)
    ax1.yaxis.set_major_formatter(FormatStrFormatter('%.1f'))
    ax1.tick_params(axis="x", labelsize=15)
    ax1.tick_params(axis="y", labelsize=15)

    ax2 = plt.subplot(122)
    ax2.plot(x_axis_1, raw_data_1, '1',
             markevery=markerSpacing, c='xkcd:red')
    ax2.plot(x_axis_1, raw_data_1, '-', markevery=markerSpacing,
             label="raw_data", c='xkcd:red')
    ax2.plot(x_axis_1, ret_gh_Val,  '2',
             markevery=markerSpacing, c='xkcd:blue')
    ax2.plot(x_axis_1, ret_gh_Val,  '-', markevery=markerSpacing,
             label="gh_filter", c='xkcd:blue')

    ax2.set_xlabel('PWM [ms]', fontsize=18)
    ax2.set_ylabel('Power [W]', fontsize=18)
    ax2.set_title('PWM/Power', fontsize=25)
    ax2.legend(loc="upper left", fontsize=15)
    ax2.set_xlim(1000, 1650)
    ax2.set_ylim(0, 20)
    ax2.grid(True)
    ax2.yaxis.set_major_formatter(FormatStrFormatter('%.1f'))
    ax2.tick_params(axis="x", labelsize=15)
    ax2.tick_params(axis="y", labelsize=15)

    plt.show()
