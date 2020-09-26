import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit

def line(_x, _k, b):
    return _x * _k + b


# noinspection PyTypeChecker
data = [(float(i[0]), float(i[1])) for i in list(map(str.split, open("data1.txt", "r").read().strip().split("\n")))]

th = [i[0] for i in data]
tc = [i[1] for i in data]

xs = []
ys = []


for i, (x, y) in enumerate(data):
    xn = tc[i] - tc[0]
    yn = sum(th[:i]) - sum(tc[1:i+1])

    xs.append(xn)
    ys.append(yn)

xs = np.array(xs)
ys = np.array(ys)

def get_error(xxs, yys, k, b):
    res = 0
    for i, (x, y) in enumerate(zip(xxs, yys)):
        res += (y - (k * x + b)) ** 2
    return res

# Fit line
(k0, b0), info = curve_fit(line, xs, ys)

A = k0
B = -1
C = b0

dists = []

for i in range(len(xs)):
    x = xs[i]
    y = ys[i]
    dist = abs(A * x + B * y + C) / np.sqrt(A**2 + B**2)
    dists.append(dist)

print(k0, b0)

plt.plot(xs, line(xs, k0, b0), color = "green", label = "Аппроксимация прямой")
plt.scatter(xs, ys, color = "red", label = "Точки")


test_point_indexes = [7, -1]
pnt0_x = xs[0]
pnt0_y = ys[0]
for tpi in test_point_indexes:
    pnt_x = xs[tpi]
    pnt_y = ys[tpi]

    k = (pnt_y - pnt0_y) / (pnt_x - pnt0_x)
    b = pnt0_y - k * pnt0_x

    print(k)

    plt.plot(xs, k * xs + (b0 + b) / 2)

plt.show()


exit(0)

err = get_error(xs, ys, k0, b0)
print(err)
print("_________")

errs = []
point_numbers = []
divs = []

for dropping_number in range(1, 10):
    (this_k, this_b), info = curve_fit(line, xs[:-dropping_number], ys[:-dropping_number])
    this_err = get_error(xs[:-dropping_number], ys[:-dropping_number], this_k, this_b)

    print(this_k, this_b)
    print(this_err / (len(xs) - dropping_number) )
    print("_________")

    errs.append(this_err)
    point_numbers.append((len(xs) - dropping_number))

    divs.append(errs[-1] / point_numbers[-1])

point_numbers = np.array(point_numbers)
divs = np.array(divs)
errs = np.array(errs)

# plt.plot(point_numbers, errs)




# leg = plt.legend(shadow = True)


# plt.show()



(this_k, this_b), info = curve_fit(line, point_numbers[:6], divs[:6])

plt.scatter(point_numbers, divs)
plt.plot(point_numbers[:6], line(point_numbers[:6], this_k, this_b))
plt.show()
