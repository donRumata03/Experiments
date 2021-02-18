from typing import Tuple

from n_ary_search import *

from approximator import *

def find_resonance(resonance_curve: Callable) -> Tuple[float, float]:
	# Find max:
	optimal_freq = n_ary_search(resonance_curve, 100, 1e-5, 1e+6, 50, 10, True)
	max_value = resonance_curve(optimal_freq)

	return optimal_freq, max_value


def get_estimator(resonance_curve: Callable):
	optimal_freq, max_value = find_resonance(resonance_curve)

	def estimator(fr):
		return -(resonance_curve(fr) - max_value / math.sqrt(2))**2

	return estimator


def count_QFactor_by_curve(resonance_curve: Callable) -> float:
	# Find max:
	optimal_freq, max_value = find_resonance(resonance_curve)

	# required_value = max_value / math.sqrt(2)
	# print(f"Looking for: {required_value} (= {max_value} / sqrt(2))", )
	estimator = get_estimator(resonance_curve) # lambda x: (resonance_curve(x) - required_value)**2

	left_window_border = n_ary_search(estimator, 300, 1e-5, optimal_freq, 100, 20, True)
	right_window_border = n_ary_search(estimator, 500, optimal_freq, 2e+4, 100, 20, True)
	print(left_window_border, right_window_border)
	print(estimator(left_window_border), estimator(right_window_border))
	# 1147.,  1328.

	dw = right_window_border - left_window_border

	return optimal_freq / dw



def graph_q_factor_finding(resonance_curve: Callable):
	optimal_freq, max_value = find_resonance(resonance_curve)

	required_value = max_value / math.sqrt(2)

	freqs = np.linspace(min([i[0] for i in real_data]), max([i[0] for i in real_data]), 1_000)
	plt.plot(freqs, configured_resonance_curve(freqs))
	plt.scatter(*zip(*real_data))
	plt.plot([0, max(freqs)], [required_value, required_value])
	plt.show()


def factor_q_factor_estimator(resonance_curve: Callable):
	est = get_estimator(resonance_curve)

	freqs = np.linspace(min([i[0] for i in real_data]), max([i[0] for i in real_data]), 1_000)
	plt.plot(freqs, est(freqs))
	plt.show()


if __name__ == '__main__':
	# graph_q_factor_finding(configured_resonance_curve)
	factor_q_factor_estimator(configured_resonance_curve)

	print("_______________________________________")
	print(f"QFactor is: {count_QFactor_by_curve(configured_resonance_curve)}")
	print(f"QFactor (analytically) is : {math.sqrt(L / c) / R}")

