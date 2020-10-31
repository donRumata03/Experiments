from scipy.optimize import curve_fit
import numpy as np

from measurements import *


def analytic_curve(voltage, mul : float):
	return voltage ** (0.5) * mul

def analytic_curve_with_undefined_pow(voltage, power, mul : float):
	return voltage ** power * mul

this_func = analytic_curve

opt, cov = curve_fit(this_func, voltages, currents)

print("Optimal values are:", opt)

print(f"COV: {cov}")

# err = np.sqrt(np.diag(cov))
# print(err)

xs = np.linspace(min(voltages), max(voltages), 1000)

if __name__ == '__main__':
	plt.scatter(voltages, currents, label = "Voltage vs. Current")
	plt.plot(xs, this_func(xs, *opt), label = "Approximation")

	plt.xlabel("Voltage, Volts")
	plt.ylabel("Current, Amperes")

	plt.show()


