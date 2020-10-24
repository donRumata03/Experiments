# eps = 4.49
# r = 250

R_known = 99.5

R_variable_min = 0.05
R_variable_max = 100.3


def get_R_by_U_known_U_total(U_known, U_total):
    I = U_known / R_known
    U_R = U_total - U_known

    return U_R / I


def get_P_by_U_known_U_total(U_known, U_total):
    I = U_known / R_known

    return I ** 2 * (R_known + get_R_by_U_known_U_total(U_known, U_total))


data = [
    # Little resistor (100 Ohm)
    (1.28, 1.29),
    (1.26, 1.34),
    (1.24, 1.40),
    (1.22, 1.43),
    (1.20, 1.50),
    (1.18, 1.54),
    (1.16, 1.59),
    (1.14, 1.64),
    (1.12, 1.70),
    (1.10, 1.74),
    (1.08, 1.79),
    (1.06, 1.84),
    (1.01, 1.98),
    (0.99, 2.01),

    # Big resistor (2.2 kOhm)
    (1.27, 1.30),
    (1.11, 1.71),
    (0.97, 2.06),
    (0.83, 2.41),
    (0.74, 2.65),
    (0.65, 2.86),
    (0.58, 3.06),
    (0.51, 3.24),
    (0.47, 3.33),
    (0.41, 3.47),
    (0.36, 3.61),
    (0.33, 3.68),
    (0.30, 3.75),
    (0.28, 3.81),
    (0.25, 3.88),
    (0.251, 3.90),
    (0.239, 3.93),
    (0.228, 3.96),
    (0.219, 3.98),
    (0.207, 4.00),
    (0.199, 4.03),
    (0.188, 4.04),
    (0.182, 4.06),
    (0.179, 4.07),
    (0.179, 4.07),

    # At peak:
    (0.96, 2.02),
    (0.80, 2.45),
    (0.85, 2.30),
    (0.92, 2.12),
    (0.78, 2.49),
    (1.07, 1.74),
]

Rs_Ps = [(get_R_by_U_known_U_total(*i), get_P_by_U_known_U_total(*i)) for i in data]
sorted_Rs_Ps = sorted(Rs_Ps)
powers = [i[1] for i in sorted_Rs_Ps]
resistances = [i[0] for i in sorted_Rs_Ps]

for i in sorted_Rs_Ps:
    print(*i)

print("Max Power is:", max(powers), "; at R = ", resistances[powers.index(max(powers))])

print(data[powers.index(max(powers)) - 2:powers.index(max(powers)) + 2])

# from matplotlib import pyplot as plt
# plt.plot(resistances, powers)

import os

the_path = "temp_plot.txt"
the_file = open(the_path, "w")
for i in sorted_Rs_Ps:
    print(*i, file=the_file)

the_file.close()

# os.system("gnuplot")
# os.system(f"plot '{the_path}' with linespoints ls 1")
