from measurements import *

import numpy as np
from scipy.optimize import curve_fit

def anal_curve(R, eps, r):
	return (R_known + R) * (eps / (r + R_known + R)) ** 2

popt, pcov = curve_fit(anal_curve, resistances, powers)

print("Optimal values are:", popt)


plt.xlabel("Resistance, Ohm")
plt.ylabel("Power, Watt")

plt.scatter(resistances, powers, label = "Measured Points")
smooth_resistances = np.linspace(min(resistances), max(resistances), 1000)
plt.plot([], [])
plt.plot(smooth_resistances, anal_curve(smooth_resistances, popt[0], popt[1]), label = "Fitted Curve")
plt.legend()
plt.show()
