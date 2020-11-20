from staphan_bolzmann_base import *

best_pow, mse_from_pow = research_graphs_pow(2, 10, 1000)

print("________________________________________________________")

print("Optimal pow is:", best_pow)

if __name__ == '__main__':
	plt.plot(*zip(*mse_from_pow))
	plt.show()

