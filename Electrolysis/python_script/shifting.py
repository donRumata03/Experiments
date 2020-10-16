from dropout import *


# Separate good and bad points:
good_index_set = set(good_point_indexes)

good_points = []
bad_points = []

for index, point in enumerate(curent_time_dependency):
	if index in good_index_set:
		good_points.append(point)
	else:
		bad_points.append(point)




