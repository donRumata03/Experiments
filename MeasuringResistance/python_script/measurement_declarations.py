import sys
sys.path.append("../../dispersion_lib")
from dispersion.dispersion import *

# Device parameters (from the previous experiment):
# eps = 7.8 	# Volts
# R_v = 697.	# Ohm
# R_e = 749.	# Ohm
# R_a = 200.	# Ohm


def convert_current(measured_current):
	return measured_current * (15.8 / 2000)

def convert_voltage(measured_voltage):
	return measured_voltage * (6.2 / 6)

current_dispersion = 0.03
voltage_dispersion = 0.1

# Scheme 1:
A1 = convert_current(dispersed_value(0.98, current_dispersion))

# Scheme 2:
V2 = convert_voltage(dispersed_value(1.5, voltage_dispersion))
A2 = convert_current(dispersed_value(0.98, current_dispersion))


# Scheme 3:
V3 = convert_voltage(dispersed_value(2.0, voltage_dispersion))


# Scheme 4:
V4 = convert_voltage(dispersed_value(2.6, voltage_dispersion))


# Scheme 5:
V5 = convert_voltage(dispersed_value(2.2, voltage_dispersion))
A5 = convert_current(dispersed_value(0.50, current_dispersion))

# Scheme 6:
A6 = convert_current(dispersed_value(1.30, current_dispersion))

# Scheme 7:
V7 = convert_voltage(dispersed_value(3.0, voltage_dispersion))
A7 = convert_current(dispersed_value(0.40, current_dispersion))

# Scheme 8:
V8 = convert_voltage(dispersed_value(2.2, voltage_dispersion))
A8 = convert_current(dispersed_value(0.50, current_dispersion))

