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
range_min_value = median - sigma
plt.plot([range_min_value, range_min_value], [0, max_density_value], linestyle = "-.", color = "#FF1111", label = "Range start")

# Median + sigma:
range_max_value = median + sigma
plt.plot([range_max_value, range_max_value], [0, max_density_value], linestyle = "--", color = "#FF1111", label = "Range end")


plt.legend()
plt.show()
