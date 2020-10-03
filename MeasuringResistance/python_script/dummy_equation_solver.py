from measurement_declarations import *

dummy_R1 = eps / A1 - R_e - R_a
dummy_R2 = 1 / (A2 / V2 - 1 / R_v)
dummy_R4 = R_v * eps / V4 - R_e - R_v
dummy_R5 = eps / A5 - R_e - R_v - R_a

# dummy_R3 = 1 / ((eps / V3 - 1) / R_e - 1 / R_v)





print(f"R1 dummyly: {dummy_R1}")
print(f"R2 dummyly: {dummy_R2}")
# print(f"R3 dummyly: {dummy_R3}")
print(f"R4 dummyly: {dummy_R4}")
print(f"R5 dummyly: {dummy_R5}")
