from measurements import *
from matplotlib import pyplot as plt

plt.scatter(*zip(*real_data))
plt.plot((theoretic_peak_freq, theoretic_peak_freq), (0, max([i[1] for i in real_data]) * 1.5))
plt.show()


# Really useful part:

class Sets:
	@property
	def ø(self):
		return set()

# def ø():
# 	return set()

sets = Sets()


all_interesting_chemistry_lessons = sets.ø

if all_interesting_chemistry_lessons:
	print("I love chemistry!")
else:
	print("I hate chemistry!")



