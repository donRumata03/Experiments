import math

from smothing_tester import *

from typing import *

def line_value(line : Tuple[float, float], _x : float):
	return _x * line[0] + line[1]


# A.K.A. «x(y)» = (y - b) / k
def inverse_line_value(line : Tuple[float, float], _y : float):
	return (_y - line[1]) / line[0]


def line_point_distance(point : Tuple[float, float], line : Tuple[float, float], add_sign : bool):
	line_A = line[0]
	line_B = -1
	line_C = line[1]

	numerator = line_A * point[0] + line_B * point[1] + line_C
	if not add_sign:
		numerator = abs(numerator)
	else:
		numerator *= -1
	denominator = np.sqrt(line_A ** 2 + line_B ** 2)

	return numerator / denominator

# print(line_point_distance((0, 0), (1, 1)))
# print(1 / math.sqrt(2))

print("Line: k =", linear_coefficients[0], ", b =", linear_coefficients[1])

# RMS for
I_diffs = np.array([p[1] for p in current_time_dependency]) - np.polyval(linear_coefficients, [p[0] for p in current_time_dependency])
t_diffs = np.array([p[0] for p in current_time_dependency]) - np.array([inverse_line_value(linear_coefficients, p[1]) for p in current_time_dependency])

print("RMS for I:", math.sqrt(
	statistics.mean(
		[(line_value(linear_coefficients, point[0]) - point[1]) ** 2 for point in current_time_dependency]
	)
))

print("RMS for I #2:", math.sqrt(
	statistics.mean(
		I_diffs ** 2  # [v**2 for v in I_diff]
	)
))

print("RMS for t:", math.sqrt(
	statistics.mean(
		t_diffs ** 2  # [v**2 for v in I_diff]
	)
))


distances_from_the_line = [line_point_distance(point, linear_coefficients, True) for point in current_time_dependency]
unsigned_distances_from_the_line = [line_point_distance(point, linear_coefficients, False) for point in current_time_dependency]
distance_distribution = count_density(distances_from_the_line, 0.1, 1000, smoothing_normal)

distance_sigma = statistics.stdev(distances_from_the_line)
print("Distance sigma is:", distance_sigma, "Mean distance is:", statistics.median(distances_from_the_line))
n_sigma = 1.5 * distance_sigma

max_allowed_distance_from_line = n_sigma

good_point_indexes = [i for i in range(len(current_time_dependency)) if line_point_distance(current_time_dependency[i], linear_coefficients, False) < max_allowed_distance_from_line]
print("Good points:", len(good_point_indexes), "/", len(current_time_dependency), good_point_indexes)


if __name__ == '__main__':
	distance_distribution_max_val = max([i[1] for i in distance_distribution])
	plt.plot([i[0] for i in distance_distribution], [i[1] for i in distance_distribution])
	plt.plot([-n_sigma, -n_sigma], [0, distance_distribution_max_val], linestyle = "--", color = "red")
	plt.plot([+n_sigma, +n_sigma], [0, distance_distribution_max_val], linestyle = "--", color = "red")
	plt.show()



