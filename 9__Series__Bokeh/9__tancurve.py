# PYTHON PROGRAM - TANGENT CURVE
from bokeh.plotting import figure, output_file, show

import numpy as np
import math
x = np.arange(0, math.pi*2, 0.05)
y = np.tan(x)

p = figure(title = "tan curve", x_axis_label = 'x', y_axis_label = 'y')

p.line(x, y, legend = "tangent(theta)", line_width = 2)

output_file("tangent.html")
show(p)