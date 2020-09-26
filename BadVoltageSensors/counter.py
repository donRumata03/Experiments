import sys
sys.path.append("./dispersion_lib")
from dispersion_lib.dispersion.dispersion import *


def convert_current(measured_current):
	return measured_current * (15.8 / 2000)

def convert_voltage(measured_voltage):
	return measured_voltage * (6.1 / 6)

# Sequentially
V1 = convert_voltage(Num_value(3.25, 0.15)) # Volts
A1 = convert_current(Num_value(0.6, 0.07)) # Amperes

# Only Ampermeter
V2 = convert_voltage(Num_value(3.7, 0.15)) # Volts

# Only Voltmeter
A3 = convert_current(Num_value(1.8, 0.15)) # Amperes

print("A1 =", A1 * 1000, "mA")
print("V1 =", V1, "V")
print("V2 =", V2, "V")
print("A3 =", A3 * 1000, "mA")


R_v = V1 / A1

R_e = (V2 - A1 * (R_v + V2 / A3)) / \
	  (A1 + (V2 * A1) / (R_v * A3) - V2 / R_v)

R_a = (V2 / A3) + (V2 / (R_v * A3)) * R_e
E = (V2 / R_v) * (R_v + R_e)

print("____________________________________________")
print(f"Rv = {R_v}")
print("Rε =", R_e)
print(f"Ra = {R_a}")
print("ε =", E)

# x = Num_value(1, 0.1)
# print(x)

# console_mode()
