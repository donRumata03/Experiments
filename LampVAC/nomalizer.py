from known_exp_approximation import *

y_noise_stddev = max(currents) / 300
new_data_amount = 10000

y_noise = np.random.normal(0, y_noise_stddev, new_data_amount)

x_noise_stddev = max(voltages) / 30
x_noise = np.random.normal(0, x_noise_stddev, new_data_amount)

clear_xs = np.linspace((voltages[0] * 3 + voltages[1]) / 4, voltages[-1], new_data_amount)
xs = clear_xs + x_noise
for i in range(len(xs)):
	if xs[i] < 0:
		xs[i] *= -1

clear_ys = np.power(xs, 3 / 5) * opt[0]
ys = clear_ys + y_noise

fake_opt, fake_cov = curve_fit(analytic_curve_with_undefined_pow, xs, ys)
temp_xs = np.linspace(voltages[0], voltages[-1], 10000)

print(f"Fake opt is: {fake_opt}")

if __name__ == '__main__':
	plt.xlabel("Voltage, Volts")
	plt.ylabel("Current, Amperes")

	plt.scatter(xs, ys)
	plt.plot(temp_xs, analytic_curve_with_undefined_pow(temp_xs, *fake_opt), label="Voltage vs. Current")
	plt.show()

# for index in range(len(voltages)):
