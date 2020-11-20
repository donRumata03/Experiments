from measurements import *

import numpy as np
from scipy.optimize import curve_fit

def power_from_resistance_anal_function(R, this_alpha, this_beta, this_gamma):
	"""
	:return: Power value
	"""
	return this_alpha * R ** 4 + this_beta * R + this_gamma


def anal_function_interference(R, this_alpha, this_beta, this_gamma):
	return this_alpha * R ** 4

def anal_function_conductivity(R, this_alpha, this_beta, this_gamma):
	return this_beta * R + this_gamma


coeffs, covariance = curve_fit(power_from_resistance_anal_function, resistances, powers)
alpha, beta, gamma = coeffs

print(f"Coeffs are: {coeffs}")

resistance_data = np.linspace(0, resistances[-1], 1000)


if __name__ == '__main__':
	matplotlib.rcParams.update({'font.size': 16})

	plt.scatter(resistances, powers, label="Resistance vs. Power")
	plt.plot(resistance_data, power_from_resistance_anal_function(resistance_data, *coeffs), label="Approximation")
	plt.plot(resistance_data, anal_function_interference(resistance_data, *coeffs), label="Radiation")
	plt.plot(resistance_data, anal_function_conductivity(resistance_data, *coeffs), label="Conductivity")

	plt.xlabel("Resistance, Ohms")
	plt.ylabel("Power, Watts")

	plt.legend()
	plt.show()

