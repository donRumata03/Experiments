from measurements import *
from scipy.optimize import curve_fit
from matplotlib import pyplot as plt
import numpy as np

def full_analytic_function(frequency, eps, resistance, capacity, inductance):
	return eps / (resistance ** 2 + (1 / (frequency * 2 * math.pi * capacity) - frequency * 2 * math.pi * inductance) ** 2) ** 0.5

def anal_function_without_c(frequency, eps, resistance, inductance):
	return full_analytic_function(frequency, eps, resistance, c, inductance)

def anal_function_without_r(frequency, eps, capacity, inductance):
	return full_analytic_function(frequency, eps, R, capacity, inductance)


def anal_function_without_L(frequency, eps, resistance, capacity):
	return full_analytic_function(frequency, eps, resistance, capacity, L)


def anal_function_without_LC(frequency, eps, resistance):
	return full_analytic_function(frequency, eps, resistance, c, L)


def anal_function_without_RC(frequency, eps, inductance):
	return full_analytic_function(frequency, eps, R, c, inductance)


def anal_function_without_RL(frequency, eps, capacity):
	return full_analytic_function(frequency, eps, R, capacity, L)


def anal_function_without_params(frequency, eps):
	return full_analytic_function(frequency, eps, R, c, L)


anal_function = anal_function_without_c


opt, cov = curve_fit(anal_function, [i[0] for i in real_data], [i[1] for i in real_data])
print(opt)


def configured_resonance_curve(frequency):
	return anal_function(frequency, *opt)



if __name__ == '__main__':
	freqs = np.linspace(min([i[0] for i in real_data]), max([i[0] for i in real_data]), 1_000)

	plt.plot(freqs, configured_resonance_curve(freqs))
	plt.scatter(*zip(*real_data))
	plt.show()
