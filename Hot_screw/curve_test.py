import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit

# Generate points on a line:
xs = np.linspace(0, 100, 20)
noise = np.random.normal(0, 10, 20)
ys = xs * 3 + 10 + noise

plt.scatter(xs, ys)
plt.show()

def line(_x, _k, b):
    return _x * _k + b

def x_n(_x, n, k, b):
    return k * _x ** n + b

def get_error(xxs, yys, k, b):
    res = 0
    for i, (x, y) in enumerate(zip(xxs, yys)):
        res += (y - (k * x + b)) ** 2
    return res

errs = []
point_numbers = []

for dropping_number in range(1, 15):
    (this_k, this_b), info = curve_fit(line, xs[:-dropping_number], ys[:-dropping_number])
    this_err = get_error(xs[:-dropping_number], ys[:-dropping_number], this_k, this_b)

    # print(this_k, this_b)
    # print(this_err / (len(xs) - dropping_number))
    errs.append(this_err)
    point_numbers.append(len(xs) - dropping_number)
    # print("_________")

errs = np.array(errs)
point_numbers = np.array(point_numbers)

(res_k, res_b), info = curve_fit(line, point_numbers, errs)
(n, k, b), info = curve_fit(x_n, point_numbers, errs)

print(n, k, b)

plt.plot(point_numbers, errs, label = "Ошибка от количества оставшихся точек")
plt.plot(point_numbers, line(point_numbers, res_k, res_b), label = "Аппроксимация прямой")
plt.plot(point_numbers, x_n(point_numbers, n, k, b), label = "Аппроксимация некоей степенью")
plt.legend(shadow = True)
plt.show()


plt.plot(point_numbers, errs / point_numbers)
plt.scatter([1000], [0])
plt.show()
