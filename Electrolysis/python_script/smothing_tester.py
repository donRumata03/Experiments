import sys
sys.path.append("../../CodeObserver")
sys.path.append("../../dispersion_lib")

from graphic_smoother import *
from dispersion.dispersion import *

import statistics
import numpy as np

from modern_measurements import *

smoothed_current_time_dependency = smooth_graph(current_time_dependency, 0.03, smoothing_normal, 1000)
linear_coefficients = np.polyfit([i[0] for i in current_time_dependency], [i[1] for i in current_time_dependency], 1)
# print(linear_coefficients)
linearly_approximated_current_time_dependency = np.polyval(linear_coefficients, [i[0] for i in current_time_dependency])
# print(linearly_approximated_current_time_dependency)

# Counting area:
print("Simple area under the curve:", count_graph_area(current_time_dependency))
print("Area under smoothed curve:", count_graph_area(smoothed_current_time_dependency))
print("Area under linearly approximated curve:", count_graph_area(zip([i[0] for i in current_time_dependency], linearly_approximated_current_time_dependency)))



# Plotting parameters:
plt.ylim(0, max([i[1] for i in current_time_dependency]) * 1.1)
plt.xlabel("t, sec")
plt.ylabel("I, A")
plt.title("Current vs. Time dependency")

# Plots:
plt.scatter([i[0] for i in current_time_dependency], [i[1] for i in current_time_dependency], label = "Original graph")
plt.plot([i[0] for i in smoothed_current_time_dependency], [i[1] for i in smoothed_current_time_dependency], label = "Smoothed graph")
plt.plot([i[0] for i in current_time_dependency], linearly_approximated_current_time_dependency, label = "Linearly approximated graph")

plt.legend()
plt.show()

