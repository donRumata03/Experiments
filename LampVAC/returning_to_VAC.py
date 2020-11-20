from resistance_vs_power_approximator import *

def U_and_I_from_R_and_P(R, P):
	P = max(0, P)

	U = (P * R) ** 0.5
	I = (P / R if R != 0 else 0) ** 0.5

	print("R:", R, "\tP:", P, "\tI:", I, "\tU:", U)

	return U, I


def U_and_I_from_R(R):
	P = power_from_resistance_anal_function(R, alpha, beta, gamma)
	return U_and_I_from_R_and_P(R, P)

def vacuum_lamp_U_and_I_from_R(R):
	P = anal_function_interference(R, alpha, beta, gamma)
	return U_and_I_from_R_and_P(R, P)


analytic_VAC = [U_and_I_from_R(resistance) for resistance in resistance_data]
# analytic_VAC = [i for i in analytic_VAC if i[0] != 0]
print(analytic_VAC)
vacuum_lamp_analytic_VAC = [vacuum_lamp_U_and_I_from_R(resistance) for resistance in resistance_data]

# print(list(zip(*analytic_VAC)))

# print(np.array().size)

if __name__ == '__main__':
	matplotlib.rcParams.update({'font.size': 16})

	plt.scatter(voltages, currents, label="Voltage vs. Current")

	plt.xlim(left=0)
	plt.ylim(bottom=0)

	plt.plot([i[0] for i in analytic_VAC], [i[1] for i in analytic_VAC], label="Analytic VAC")
	plt.plot([i[0] for i in vacuum_lamp_analytic_VAC], [i[1] for i in vacuum_lamp_analytic_VAC], label="Vacuum Lamp's Analytic VAC")

	plt.xlabel("Voltage, Volts")
	plt.ylabel("Current, Amperes")

	plt.legend()
	plt.show()
