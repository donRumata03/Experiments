mark_eps = 4.39
mark_R_a = 116
mark_R_v = 735
mark_R_e = 224


andrews_eps = 4.7
andrews_R_a = 110
andrews_R_v = 680
andrews_R_e = 260


eps = (mark_eps + andrews_eps) / 2
R_a = (mark_R_a + andrews_R_a) / 2
R_v = (mark_R_v + andrews_R_v) / 2
R_e = (mark_R_e + andrews_R_e) / 2

print(f"Rv = {R_v} Ohm")
print("Rε =", R_e, "Ohm")
print(f"Ra = {R_a} Ohm")
print("ε =", eps, "Volts")
print("____________________________________________")

