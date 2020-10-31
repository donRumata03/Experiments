from measurements import *

from scipy.optimize import minimize
import numpy as np
import scipy

resistances = [voltages[i] / currents[i] for i in range(1, len(voltages))]
resistances.insert(0, resistances[0])

for index, T in enumerate(resistances):
	print(f"T{index} =  {T}` / k`")


# Trying to determine: k, alpha, sigma

T_out = 300  # Kelvins

def sigma_equation_error_function(arg):
	this_k, this_alpha, this_sigma = arg

	if this_k == 0:
		this_k = 1e-3

	res = 0
	for i in range(len(resistances)):
		temperature = resistances[i] / this_k
		res += this_sigma * temperature ** 4 \
				+ temperature * this_alpha \
				+ resistances[i] * currents[i] ** 2 \
				- this_alpha * T_out

	return abs(res)


optimization_res = scipy.optimize.newton_krylov(sigma_equation_error_function, [0, 0, 0], f_tol=1e-11)  # minimize(sigma_equation_error_function, [0, 0, 0], method = "COBYLA")

print(optimization_res)

print(sigma_equation_error_function([0,  0,  1e-8]))

