import json
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
	return initial_date + timedelta(days=int(day_index))

def date_to_day_index(this_date: date):
	return (this_date - initial_date).days

all_measured_day_indices = list(range(n_days))
all_measured_dates = [day_index_to_date(i) for i in all_measured_day_indices]

########

def process_measurement_data(data: List[Tuple[int, float]]):
	return [(day_index_to_date(measurement[0]), math.atan(measurement[1])) for measurement in data]

def convert_data_to_day_indexes(data):
	return [
		(date_to_day_index(i[0]), i[1]) for i in data
	]

def convert_data_to_dates(data):
	return [
		(day_index_to_date(i[0]), i[1]) for i in data
	]

def convert_radians_to_degrees(data):
	return [
		(i[0], math.degrees(i[1])) for i in data
	]

def convert_degrees_to_radians(data):
	return [
		(i[0], math.radians(i[1])) for i in data
	]

# Data:         ( Day index | measured tangent ) --> converted to   ( Date | degree )


vova_house_h = 28.5

real_data_by_vova = process_measurement_data([
		(1, vova_house_h / 75),
		(2, vova_house_h / 70)
])


andrew_house_height = 14.
andrew_stick_height = 1.205
_raw_real_data_by_andrew = [
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
]
real_data_by_andrew = process_measurement_data(_raw_real_data_by_andrew)

real_data_by_sergey = process_measurement_data([
		(3, math.tan(math.radians(17))),
		(46, math.tan(math.radians(3.4))),
])

real_data_by_nikita = process_measurement_data([
		(47, math.tan(math.radians(5))),
])


all_real_data = sorted(
	real_data_by_vova[:] +
	real_data_by_andrew[:] +
	real_data_by_sergey[:] +
	real_data_by_nikita[:]
)

good_real_data = sorted(
	real_data_by_andrew[:] +
	real_data_by_sergey[:] +
	real_data_by_nikita[:]
)


def print_measurement_data(data):
	print(
		json.dumps(
			[(i[0].__str__(), i[1]) for i in data],
			indent=1
		)
	)

if __name__ == '__main__':
	print_measurement_data(all_real_data)
	print(_raw_real_data_by_andrew)
	print(day_index_to_date(0))


# real_measurement_data = [
#
# ]

