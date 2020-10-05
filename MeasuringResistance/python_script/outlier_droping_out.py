from dummy_equation_solver import *

import sys
sys.path.append("../../CodeObserver")

from graphic_smoother import *

distribution_density = count_density(all_resistances, 0.3, 100)
print(distribution_density)

