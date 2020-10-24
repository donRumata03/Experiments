from typing import Tuple

from device_parameters import *
from measurement_declarations import *

def equation_1_for_optimizing(this_r : float) -> Tuple[float, float]:
	return eps, A1.value * (R_e + R_a + this_r)

def equation_2_for_optimizing(this_r : float) -> Tuple[float, float]:
	return V2.value, A2.value / (1 / R_v + 1 / this_r)

def equation_3_for_optimizing(this_r : float) -> Tuple[float, float]:
	r_all = 1 / (1 / R_v + 1 / this_r)

	return V3.value, eps * r_all / (R_e + r_all)

def equation_4_for_optimizing(this_r : float) -> Tuple[float, float]:
	return V4.value, eps * R_v / (R_e + R_v + this_r)

def equation_5_for_optimizing(this_r : float) -> Tuple[float, float]:
	return eps, A5.value * (this_r + R_e + R_a + R_v)


all_equations_for_optimizing = [
	equation_1_for_optimizing,
	equation_2_for_optimizing,
	equation_3_for_optimizing,
	equation_4_for_optimizing,
	equation_5_for_optimizing,
]


