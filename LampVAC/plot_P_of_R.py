from measurements import *

if __name__ == '__main__':
	matplotlib.rcParams.update({'font.size': 16})
	plt.scatter(resistances, powers, label="Resistance vs. Power")
	plt.xlabel("Resistance, Ohms")
	plt.ylabel("Power, Watts")

	plt.legend()
	plt.show()

