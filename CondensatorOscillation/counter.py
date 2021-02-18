from math import exp, log

def get_old_U0(t1, U1, t2, U2):
	print((exp(t2) - exp(t1)))
	return U1 + (U1 - U2) / (exp(t2) - exp(t1))


def get_old_tao(t1, U1, t2, U2, U0):
	minus_inverted_exped_tao = (U1 - U2) / ( (exp(t2) - exp(t1)) * U0 )
	tao = - 1 / log(minus_inverted_exped_tao)

def get_U0(t1, U1, t2, U2):
	pass
	# todo return U1 + (U1 - U2) / (exp(t2) - exp(t1))


def get_tao(t1, U1, t2, U2):
	return (t1 - t2) / (log(U1 / U2))



measured_t1 = 0
measured_U1 = 0

measured_t2 = 2.6 * 10**-3 # 2.6 Milliseconds
measured_U2 = 15 # 15 Volts

computed_U0 = get_U0(
	measured_t1, measured_U1,
	measured_t2, measured_U2,
)

print(f"U0 is {computed_U0}")

computed_tao = get_tao(
	measured_t1, measured_U1,
	measured_t2, measured_U2,
	# computed_U0
)

print(f"τ is {computed_tao}")

