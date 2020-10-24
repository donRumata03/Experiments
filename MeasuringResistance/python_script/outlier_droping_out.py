from dummy_equation_solver import *

import sys
sys.path.append("../../CodeObserver")

from graphic_smoother import *
from dummy_equation_solver import *
from matplotlib import pyplot as plt
import statistics

median = statistics.mean(all_resistance_values)
sigma = statistics.stdev(all_resistance_values)

print("____________________________________________")
print("Mean value is:", median)
print("Standard deviation is:", sigma)

range_min_value = median - sigma
range_max_value = median + sigma

satisfies_range = lambda x: range_min_value <= x <= range_max_value

used_resistances = [value for value in all_resistance_values if satisfies_range(value)]
used_resistance_indexes = [index for (index, value) in enumerate(all_resistance_values) if satisfies_range(value)]

used_dispersion_sum = 0
for r_index in used_resistance_indexes:
	used_dispersion_sum += all_resistance_dispersions[r_index]

resistance_dispersion_average = used_dispersion_sum / len(used_resistance_indexes)
resultant_resistance_dispersion = resistance_dispersion_average / (len(used_resistance_indexes) / 2)
print("Resultant resistance dispersion:", resultant_resistance_dispersion)

print("Resistances left after dropping out: ", used_resistances)

if __name__ == '__main__':
	from equation_solving_optimization import optimal_r
	print("Optimal R is:", optimal_r)

	distribution_density = count_density(all_resistance_values, 0.1, 1000, smoothing_normal)
	# print(distribution_density)

	# Distribution:
	plt.plot([i[0] for i in distribution_density], [i[1] for i in distribution_density])

	# Points
	plt.scatter(all_resistance_values, [0] * len(all_resistance_values), color="red", edgecolors = "darkred", s=[200]*len(all_resistance_values))

	# Median:
	max_density_value = max([i[1] for i in distribution_density])
	print(f"Max density value is {max([i[1] for i in distribution_density])}")
	plt.plot([median, median], [0, max_density_value], linestyle = ":", label = "Median", color = "#0FD00F")

	# Median - sigma:
	plt.plot([range_min_value, range_min_value], [0, max_density_value], linestyle = "-.", color = "#FF1111", label = "Range start")

	# Median + sigma:
	plt.plot([range_max_value, range_max_value], [0, max_density_value], linestyle = "--", color = "#FF1111", label = "Range end")

	# Optimal R value:
	plt.plot([optimal_r, optimal_r], [0, max_density_value], linestyle = "-.", color = "cyan", label = "Optimal resistance", linewidth = 5)

	plt.legend()
	plt.show()
