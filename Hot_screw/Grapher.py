import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit


data = [(float(i[0]), float(i[1])) for i in list(map(str.split, open("data1.txt", "r").read().strip().split("\n")))]

def line(_x, _k, b):
    return _x * _k + b

def exponent(_x, a, b, c):
    return c + a * np.exp(-b * _x)

to_plot_xs = []
to_plot_ys = []
indexes = []

for i, (x, y) in enumerate(data):
    xn = x
    yn = y
    to_plot_xs.append(x)
    to_plot_ys.append(y)
    indexes.append(i)

indexes = np.array(indexes)
to_plot_xs = np.array(to_plot_xs)
to_plot_ys = np.array(to_plot_ys)

line_x, p_cov_x = curve_fit(line, indexes, to_plot_xs)
line_y, p_cov_y = curve_fit(line, indexes, to_plot_ys)

exp_x, _ = curve_fit(exponent, indexes, to_plot_xs, maxfev = 1000000, )
exp_y, __ = curve_fit(exponent, indexes, to_plot_ys, maxfev = 1000000)

line_err = 0
exp_err = 0

for i in indexes:
    line_err += (line(i, *line_y) - to_plot_ys[i]) ** 2
    exp_err += (exponent(i, *exp_y) - to_plot_ys[i]) ** 2

print("Line err:", line_err)
print("Exp err:", exp_err)

print("Difference:", line_err / exp_err)

# plt.plot(indexes, line(indexes, *line_x))
# plt.plot(indexes, exponent(indexes, *exp_x))
# plt.plot(indexes, to_plot_xs)

plt.plot(indexes, line(indexes, *line_y), label = "Аппроксимация прямой")
plt.plot(indexes, exponent(indexes, *exp_y), label="Аппроксимация экспонентой")
plt.plot(indexes, to_plot_ys, label = "Исходные данные")

leg = plt.legend()

plt.show()
