import numpy as np

from outlier_droping_out import *
from equations_to_optimize import *

use_resistances_as_weights = True

def error_function(this_resistance : float, weighted : bool):
	res : float = 0.

	for precise_equation_index in used_resistance_indexes:
		this_equation = all_equations_for_optimizing[precise_equation_index]
		# print(f"Adding equation №{precise_equation_index}: {this_equation}")
		equation_sides = this_equation(this_resistance)
		equation_left, equation_right = equation_sides

		weight = 1 if not weighted else (1 / all_resistance_dispersions[precise_equation_index])

		res += weight * (equation_left - equation_right) ** 2

	return res

min_possible_resistance = min(used_resistances)
max_possible_resistance = max(used_resistances)

all_theoretically_possible_resistance_values = np.linspace(min_possible_resistance, max_possible_resistance, 10000)

error_function_results = [error_function(resistance, use_resistances_as_weights) for resistance in all_theoretically_possible_resistance_values]

optimal_r = min([(value, index) for (value, index) in zip(error_function_results, all_theoretically_possible_resistance_values)])[1]
print("Optimal R is", optimal_r)


if __name__ == "__main__":
	plt.xlabel("R")
	plt.ylabel("Error function value")

	# Error:
	plt.plot(all_theoretically_possible_resistance_values, error_function_results, label = "Error function vs. chosen Resistance")

	# Solution:
	max_error_function_value = max(error_function_results)
	min_error_function_value = min(error_function_results)
	error_max_delta = max_error_function_value - min_error_function_value


	plt.plot([optimal_r, optimal_r], [min_error_function_value - error_max_delta * 0.05, max_error_function_value], linestyle = "--", label = "Optimal R value")

	plt.legend()
	plt.show()
