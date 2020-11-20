import math
from typing import Tuple

from measurements import *

import statistics
import numpy as np
from scipy.optimize import curve_fit


def mse(function, points):
	return statistics.median(
		[(function(point[0]) - point[1])**2 for point in points]
	)

####################################

def power_from_resistance_anal_function_without_bolzmann(R, this_alpha, this_beta, this_gamma, this_bolzmann_power):
	"""
	:return: Power value
	"""

	# if this_bolzmann_power >= 5 or this_bolzmann_power <= 3:
	# 	return math.inf

	return this_alpha * R ** this_bolzmann_power + this_beta * R + this_gamma


def get_n_th_pow_function(n):
	return lambda R, this_alpha, this_beta, this_gamma: \
		power_from_resistance_anal_function_without_bolzmann(R, this_alpha, this_beta, this_gamma, n)


def research_graphs_pow(left, right, point_number, logging: bool = True) -> Tuple[float, list]:
	best_value = math.inf
	best_pow = None

	mse_from_pow = []

	for this_n in np.linspace(left, right, point_number):
		coeffs, covariance = curve_fit(get_n_th_pow_function(this_n), resistances, powers)
		alpha_for_n, beta_for_n, gamma_for_n = coeffs
		# print(f"Coeffs are: {coeffs}")

		this_mse = mse(
			lambda this_R: get_n_th_pow_function(this_n)(this_R, alpha_for_n, beta_for_n, gamma_for_n),
			zip(resistances, powers)
		)

		mse_from_pow.append((this_n, this_mse))

		if best_value > this_mse:
			best_value = this_mse
			best_pow = this_n

		if logging:
			print(
				this_n, ":",
				this_mse
			)

	return best_pow, mse_from_pow

