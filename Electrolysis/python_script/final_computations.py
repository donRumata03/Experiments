from shifting import *

Q = dispersed_value(predicted_area, average_dS)

Z_Cu_2p = 2
M_Cu = 63.546 / 1000

F = (M_Cu / Z_Cu_2p) * Q / dm

print("dM =", dm * 1000)
print("Q =", Q, "Qulones")

print("F =", F)
