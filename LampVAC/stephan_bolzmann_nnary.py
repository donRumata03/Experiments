from staphan_bolzmann_base import *


def n_ary_search(depth_left, left, right, n_arity, ns) -> float:
	if depth_left == 0:
		return (left + right) / 2

	step = (right - left) / n_arity
	offset = step * ns

	best_pow, mse_from_pow = research_graphs_pow(left, right, n_arity, False)

	return n_ary_search(depth_left - 1, best_pow - offset, best_pow + offset, n_arity, ns)


values = []
for recursion_limit in range(1, 16):
	value = n_ary_search(recursion_limit, 2, 10, 100, 30)

	values.append((recursion_limit, value))

	print(value)

print(values)

if __name__ == '__main__':
	matplotlib.rcParams.update({'font.size': 16})

	plt.title("N-ary search Dynamic")

	plt.plot(*zip(*values))

	plt.xlabel("Iteration's Index")
	plt.ylabel("MSE")

	plt.show()

