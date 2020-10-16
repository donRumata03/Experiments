from measurements import *

import sys
sys.path.append("../../CodeObserver")

from graphic_smoother import *

smoothed_dependency = smooth_graph(all_time_current_points, 0.1, smoothing_normal)
print(smoothed_dependency)
