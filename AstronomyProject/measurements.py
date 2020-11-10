import math
import numpy as np
from typing import *
from datetime import date, timedelta



n_days = 48
initial_date = date(2020, 9, 24)

"""
	Day index starts from zero for the first measurement day and is [0, n_days)
	
	In GoogleDocs(https://docs.google.com/spreadsheets/d/1F_DoQ4brBQePHNCiOVG615uoBIPiO2jDlzrxd8Wwrc4/):
		date index is `row_number - 2`
"""
def day_index_to_date(day_index: int):
	assert day_index < n_days
	initial_date + timedelta(days=day_index)

def date_to_day_index(this_date: date):
	return (this_date - initial_date).days

########

def process_measurement_data(data: List[Tuple[int, float]]):
	return [(day_index_to_date(measurement[0] - 2), math.atan(measurement[1])) for measurement in data]

# Data:         ( Day index | measured tangent ) --> converted to   ( Date | degree )


real_data_by_vova = process_measurement_data([

])


andrew_house_height = 14.
andrew_stick_height = 1.205
real_data_by_andrew = process_measurement_data([
	# Nothing for day 0
	(1, andrew_house_height / (45 + 0.0)),
	(2, andrew_house_height / (45 + 2.3)),

	(6, andrew_house_height / (45 + 9.2)),
	(7, andrew_house_height / (45 + (8.7 * 2 + 10.4 * 1) / (2 + 1))),
	(8, andrew_house_height / (45 + 10.2)),

	# HALYAVA

	(20, andrew_house_height / (45 + 31.)),

	# BIG HALYAVA

	(38, andrew_stick_height / 8.65),

	# Little HALYAVA

	(47, andrew_stick_height / 17.5)
])

real_data_by_sergey = process_measurement_data([

])

real_data_by_nikita = process_measurement_data([

])


all_real_data = sorted(
	real_data_by_vova[:] +
	real_data_by_andrew[:] +
	real_data_by_sergey[:] +
	real_data_by_nikita[:]
)

if __name__ == '__main__':
	print(all_real_data)
	print(day_index_to_date(0))


# real_measurement_data = [
#
# ]

