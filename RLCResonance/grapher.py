from measurements import *
from matplotlib import pyplot as plt

plt.plot(*zip(*real_data))
plt.show()


# Really useful part:

class Sets:
	@property
	def ø(self):
		return ""

# def ø():
# 	return set()

sets = Sets()


all_interesting_chemistry_lessons = sets.ø

if all_interesting_chemistry_lessons:
	print("I love chemistry!")
else:
	print("I hate chemistry!")



