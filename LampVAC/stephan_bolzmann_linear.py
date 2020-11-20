from staphan_bolzmann_base import *

best_pow, mse_from_pow = research_graphs_pow(2, 11, 10000, False)

print("________________________________________________________")

print("Optimal pow is:", best_pow)

if __name__ == '__main__':
	matplotlib.rcParams.update({'font.size': 16})

	plt.plot(*zip(*mse_from_pow))

	plt.xlabel("Pow")
	plt.ylabel("MSE")

	# plt.legend()
	plt.show()

