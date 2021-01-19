import math

R_L = 86.1
R_R = 1243.
R = R_L + R_R

c = 292e-9
L = 1.425

theoretic_peak_freq = 1 / (math.sqrt(L * c) * 2 * math.pi)
print(f"According to theory, the peak should be at frequency {theoretic_peak_freq}")


experiments = [
	{
		"voltage_step": 2.,
		"time_step": 50, # ms
		"data": [
			# horizontal 1/5's (of 1/2 period)  |   vertical 1/5's
			(14,                                        32),
		]
	},
	{
		"voltage_step": 2.,
		"time_step": 20, # ms
		"data": [
			# horizontal 1/5's (of 1/2 period)  |   vertical 1/5's
			(26,                                        30),
			(24,                                        28),
			(22.5,                                      26),
			(16,                                        19),
			(15,                                        16),
			(14,                                        13),
		]
	}
]

real_data = []

for experiment in experiments:
	for data_piece in experiment["data"]:
		print("Steps in period =", (data_piece[0] / 5) * 2)
		period = experiment["time_step"] / 1000 * (data_piece[0] / 5) * 2
		freq = 1 / period
		amplitude = experiment["voltage_step"] * (data_piece[1] / 5) / 2
		real_data.append((freq, amplitude))

print(real_data)
