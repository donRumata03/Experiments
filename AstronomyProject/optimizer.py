from graph_plotter import *

from scipy.optimize import curve_fit

def analytic_curve_line(x, k, b):
	return k * x + b

def analytic_curve_sine(x, mul, w, fi0, shift):
	return mul * (np.sin(w * x + fi0) + shift)

used_approximation = analytic_curve_line

data_for_training = convert_data_to_day_indexes(good_real_data)
x_data_for_training = [i[0] for i in data_for_training]
y_data_for_training = [i[1] for i in data_for_training]

sample_opt = (0.11717760484940531, 0.07, 0 * 2 * math.pi, 1.6072776280619603)

opt, cov = curve_fit(used_approximation, x_data_for_training, y_data_for_training)
# opt = sample_opt


# print(f"k = {opt[0]}, b = {opt[1]}")
print(f"Optimal parameters are:", *opt)

# Generate Points:
x_data_sampled = np.array(all_measured_day_indices) # np.linspace(min(x_data_for_training), max(x_data_for_training), 1000)
y_data_sampled = used_approximation(x_data_sampled, *opt)
raw_data_sampled = zip(x_data_sampled, y_data_sampled)
data_sampled_radians = convert_data_to_dates(raw_data_sampled)
data_sampled_degrees = convert_radians_to_degrees(data_sampled_radians)

if __name__ == '__main__':
	set_plot_formatter()

	add_date_data_to_plot(good_real_data, "Data")
	# add_date_data_to_plot(data_sampled, "Approximation")
	plt.plot(*zip(*data_sampled_degrees), label="Approximation")

	print(*zip(*data_sampled_degrees))

	setup_plot_finishing()
