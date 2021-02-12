import math

R_L = 288 # 86.1
R_R = 1249 # 1243.
R = R_L + R_R

c = 13.4e-9 # 292e-9
L = 1.443 # 1.425

theoretic_peak_freq = 1 / (math.sqrt(L * c) * 2 * math.pi)
print(f"According to theory, the peak should be at frequency {theoretic_peak_freq}")


old_experiments = [
	# Old:

	# {
	# 	"voltage_step": 2.,
	# 	"time_step": 50, # ms
	# 	"data": [
	# 		# horizontal 1/5's (of 1/2 period)  |   vertical 1/5's
	# 		(14,                                        32),
	# 	]
	# },
	# {
	# 	"voltage_step": 2.,
	# 	"time_step": 20, # ms
	# 	"data": [
	# 		# horizontal 1/5's (of 1/2 period)  |   vertical 1/5's
	# 		(26,                                        30),
	# 		(24,                                        28),
	# 		(22.5,                                      26),
	# 		(16,                                        19),
	# 		(15,                                        16),
	# 		(14,                                        13),
	# 	]
	# }
	{
		"voltage_step": 0.05,
		"time_step": 2,
		"data": [

		]
	}
]

new_experiments = [
	{
		"voltage_step": 0.05,
		# "time_step": 2,
		"data": [
			(100, 30),
		]
	},
	{
		"voltage_step": 0.1,
		# "time_step": 2,
		"data": [
			(120, 18),
			(140, 21),
			(160, 25),
			(180, 28),
		]
	},
	{
		"voltage_step": 0.2,
		"data": [
			(200, 16.5),
			(230, 18),
			(250, 19),
			(300, 24),
			(350, 29),
		]
	},
	{
		"voltage_step": 0.5,
		"data": [
			(400, 14),
			(500, 18),
			(550, 22),
			(550, 22),
			(600, 23),
			(650, 28),
			(700, 29),
		]
	},
	{
		"voltage_step": 1.,
		"data": [
			(750, 17),
			(800, 20),
			(850, 24),
			(900, 26),
		]
	},
	{
		"voltage_step": 2.,
		"data": [
			(950, 18),
			(1000, 20),
			(1050, 29),
			# (1050, 29),
		]
	},
	{
		"voltage_step": 5.,
		"data": [
			(1100, 13),
			(1150, 17),
			(1200, 23),
			(1250, 24),
			(1300, 22),
			(1350, 13),
			(1400, 13),
			(1450, 10),
		]
	},
	{
		"voltage_step": 2.,
		"data": [
			(1500, 22),
		]
	},
	{
		"voltage_step": 0.2,
		"data": [
			(4000, 24),
		]
	},
	{
		"voltage_step": 0.5,
		"data": [
			(2500, 23),
			(3000, 16),
		]
	},
	{
		"voltage_step": 1.,
		"data": [
			(2000, 18),
		]
	}
]

real_data = []

for experiment in old_experiments:
	for data_piece in experiment["data"]:
		print("Steps in period =", (data_piece[0] / 5) * 2)
		period = experiment["time_step"] / 1000 * (data_piece[0] / 5) * 2
		freq = 1 / period
		amplitude = experiment["voltage_step"] * (data_piece[1] / 5) / 2
		real_data.append((freq, amplitude))

for experiment in new_experiments:
	for data_piece in experiment["data"]:
		amplitude = experiment["voltage_step"] * (data_piece[1] / 5) / 2
		real_data.append((data_piece[0], amplitude))


print(real_data)
