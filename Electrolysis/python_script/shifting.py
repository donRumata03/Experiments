from dropout import *


# Separate good and bad points:
good_index_set = set(good_point_indexes)

good_points = []
bad_points = []

for index, point in enumerate(current_time_dependency):
	if index in good_index_set:
		good_points.append(point)
	else:
		bad_points.append(point)

# print(good_points)
# print(bad_points)

smallest_good_point_with_distance = min([(line_point_distance(point, linear_coefficients, True), point) for index, point in enumerate(good_points)])
biggest_good_point_with_distance = max([(line_point_distance(point, linear_coefficients, True), point) for index, point in enumerate(good_points)])

smallest_good_point = smallest_good_point_with_distance[1]
biggest_good_point = biggest_good_point_with_distance[1]

upper_line = (linear_coefficients[0], linear_coefficients[1] - line_value(linear_coefficients, biggest_good_point[0]) + biggest_good_point[1])
bottom_line = (linear_coefficients[0], linear_coefficients[1] - line_value(linear_coefficients, smallest_good_point[0]) + smallest_good_point[1])

# print("Upper line is:", upper_line)

lowest_area = count_graph_area(zip([i[0] for i in current_time_dependency], np.polyval(bottom_line, [i[0] for i in current_time_dependency])))
highest_area = count_graph_area(zip([i[0] for i in current_time_dependency], np.polyval(upper_line, [i[0] for i in current_time_dependency])))
print("Min possible area:", lowest_area)
print("Max possible area:", highest_area)

upper_dS = highest_area - count_graph_area(smoothed_current_time_dependency)
lower_dS = count_graph_area(smoothed_current_time_dependency) - lowest_area
average_dS = (upper_dS + lower_dS) / 2

print("dx's:", lower_dS, upper_dS, average_dS)

if __name__ == '__main__':
	plt.ylim(0, max([i[1] for i in current_time_dependency]) * 1.1)
	plt.xlabel("t, sec")
	plt.ylabel("I, A")
	plt.title("Current vs. Time dependency")
	plt.plot([i[0] for i in current_time_dependency], linearly_approximated_current_time_dependency, label = "Linearly approximated graph")
	plt.scatter([i[0] for i in good_points], [i[1] for i in good_points], color = "green", label = "Close points")
	plt.scatter([i[0] for i in bad_points], [i[1] for i in bad_points], color = "red", label = "Faraway points")

	plt.plot([i[0] for i in current_time_dependency], np.polyval(upper_line, [i[0] for i in current_time_dependency]),
		color = "red", linestyle = "--", label = "Upper line")
	plt.plot([i[0] for i in current_time_dependency], np.polyval(bottom_line, [i[0] for i in current_time_dependency]),
		color = "red", linestyle = "--", label = "Lower line")

	plt.legend()
	plt.show()




