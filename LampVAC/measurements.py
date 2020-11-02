#           Voltage, Current:

data = [
    (0.00, 0.00),
    (0.82, 0.08),
    (0.96, 0.09),
    (1.52, 0.11),
    (1.56, 0.11),
    (1.68, 0.12),
    (1.80, 0.12),
    (2.22, 0.13),
    (2.26, 0.14),
    (2.36, 0.14),
    (2.53, 0.14),
    (2.69, 0.15),
    (2.84, 0.16),
    (2.94, 0.16),
    (3.15, 0.16),
    (3.51, 0.17),
    (3.80, 0.18),
    (4.03, 0.19),
    (4.51, 0.20),
    (5.25, 0.21),
    (6.07, 0.23),

    (0.59, 0.06),
    (1.08, 0.09),
    (1.19, 0.10),
    (1.58, 0.11),
    (2.82, 0.15),
    (3.06, 0.16),
    (1.69, 0.12),
]

data.sort(key=lambda pair: pair[0])

voltages = [i[0] for i in data]
currents = [i[1] for i in data]


import os
if os.name == "posix":
    print("F_cking Linux!")
    exit(0)

from matplotlib import pyplot as plt

voltages = [i[0] for i in data]
currents = [i[1] for i in data]

if __name__ == '__main__':
    plt.scatter(voltages, currents, label="Voltage vs. Current")

    plt.xlabel("Voltage, Volts")
    plt.ylabel("Current, Amperes")

    plt.show()


