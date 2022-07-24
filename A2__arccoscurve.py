# PYTHON PROGRAM - ARCCOS() CURVE
from bokeh.plotting import figure, output_file, show

import numpy as np
import math
#x = np.arange(0, math.pi*2, 0.05)
x = np.arange(-1, +1, 0.05)
y = np.arccos(x)

p = figure(title = "arccos curve", x_axis_label = 'x', y_axis_label = 'y')

p.line(x, y, legend = "arccos()", line_width = 2)

output_file("arccosine.html")
show(p)