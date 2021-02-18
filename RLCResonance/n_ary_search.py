from typing import Callable
from sys import setrecursionlimit
setrecursionlimit(int(1e+9))

def n_ary_search(function: Callable, depth_left: int, left: float, right: float, n_arity: int, ns : int, max_or_min: bool = True) -> float:
	# print(depth_left, ": [", left, ";", right, "]")
	if depth_left == 0:
		return (left + right) / 2

	step = (right - left) / n_arity
	offset = step * ns

	optimal_x = None
	optimal_value = None
	for step_index in range(n_arity + 1):
		this_x = left + step * step_index
		this_value = function(this_x)
		if optimal_x is None or (this_value > optimal_value if max_or_min else this_value < optimal_value):
			optimal_x = this_x
			optimal_value = this_value

	return n_ary_search(function, depth_left - 1, max(left, optimal_x - offset), min(right, optimal_x + offset), n_arity, ns)



if __name__ == '__main__':
	# Test n_ary_search (the answer is ≈3):
	print(n_ary_search(lambda x: -(x - 3)**2 + 10, 100, -10, +10, 100, 20, True))


