# PYTHON PROGRAM - SOSINE CURVE
from bokeh.plotting import figure, output_file, show

import numpy as np
import math
x = np.arange(0, math.pi*2, 0.05)
y = np.cos(x)

p = figure(title = "cosine wave example", x_axis_label = 'x', y_axis_label = 'y')

p.line(x, y, legend = "cosine", line_width = 2)

output_file("cosine.html")
show(p)