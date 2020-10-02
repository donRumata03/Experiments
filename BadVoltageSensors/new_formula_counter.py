import sys
sys.path.append("./dispersion_lib")
from dispersion_lib.dispersion.dispersion import *


def convert_current(measured_current):
	return measured_current * (15.8 / 2000)

def convert_voltage(measured_voltage):
	return measured_voltage * (6.1 / 6)

# Sequentially
V1 = convert_voltage(dispersed_value(3.25, 0.03)) # Volts
A1 = convert_current(dispersed_value(0.6, 0.07)) # Amperes

# Only Ampermeter
V2 = convert_voltage(dispersed_value(3.7, 0.03)) # Volts

# Only Voltmeter
A3 = convert_current(dispersed_value(1.8, 0.07)) # Amperes

print("A1 =", A1 * 1000, "mA")
print("V1 =", V1, "V")
print("V2 =", V2, "V")
print("A3 =", A3 * 1000, "mA")

# The actual calculation:

R_v = V1 / A1

R_a = ( A1 * R_v + (V2 * A1) / (A3 - V2 / R_v) - V2 - V2 ** 2 / (R_v * A3 - V2) ) / \
 	  ( (A3 * V2) / (A3 * R_v - V2) - A1 * (1 + A3 / (A3 - V2 / R_v)) )

R_e = (V2 + A3 * R_a) / (A3 - V2 / R_v)

eps = V2 * (1 + (R_e / R_v))  # (V2 / R_v) * (R_v + R_e)

print("____________________________________________")
print(f"Rv = {R_v} Ohm")
print("Rε =", R_e, "Ohm")
print(f"Ra = {R_a} Ohm")
print("ε =", eps, "Volts")

# x = Num_value(1, 0.1)
# print(x)

# console_mode()

# Validate results:

print("A1 = ε / (R_v + R_e + R_A) : ", A1, "?=", eps  / (R_v + R_e + R_a))
print("V1 = ε * R_v / (R_v + R_e + R_A)", V1, "?=", eps * R_v / (R_v + R_e + R_a))
print("V2 = ε * R_v / (R_v + R_e)", V2, "?=", eps * R_v / (R_v + R_e))
print("A3 = ε / (R_a + R_e)", A3, "?=", eps / (R_a + R_e))