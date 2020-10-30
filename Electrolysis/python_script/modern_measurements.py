import statistics

from matplotlib import pyplot as plt
import sys

sys.path.append("../../dispersion_lib")

from dispersion.dispersion import *


m_cathode_0 =  dispersed_value(8.90, 0.03) / 1000.   # Is 8.90 grams ± 0.03 grams
m_cathode_1 = dispersed_value(9.29, 0.03) / 1000.   #

m_anode_0 = dispersed_value(36.49, 0.03) / 1000.   #
m_anode_1 = dispersed_value(35.96, 0.03) / 1000.   #

dm = m_anode_0 - m_anode_1

current_time_dependency = list(map(lambda x: (float(x.split()[0]), float(x.split()[1])), open("Measurements.txt", "r").read().split("\n")[1:]))

t_s = [i[0] for i in current_time_dependency]
I_s = [i[1] for i in current_time_dependency]

print(statistics.stdev(t_s) ** 2, statistics.stdev(I_s) ** 2)

if __name__ == '__main__':
	print("dM is", dm * 1000, "grams")

	plt.ylim(0, max([i[1] for i in current_time_dependency]) * 1.1)
	plt.xlabel("t, sec")
	plt.ylabel("I, A")
	plt.title("Current vs. Time dependency")
	plt.scatter([i[0] for i in current_time_dependency], [i[1] for i in current_time_dependency])
	plt.show()
