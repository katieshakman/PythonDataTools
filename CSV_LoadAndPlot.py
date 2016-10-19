# Katie Shakman 10/19/2016
# Based on: http://blog.bharatbhole.com/creating-boxplots-with-matplotlib/

from sys import argv

import numpy as np

import pandas as pd

import matplotlib as mpl
import matplotlib.pyplot as plt

# Get CSV filename from input argument:
filename = argv[1]

# Set up to save plot as .png:
mpl.use('agg')

# Open CSV and save data as a variable:
data = pd.read_csv(filename)
print data
plotData = [data.A, data.B, data.C]
print plotData

# Plot data as boxplot
fig = plt.figure(1, figsize=(9,6))
ax = fig.add_subplot(111)
bp = ax.boxplot(plotData)

# Save figure:
fig.savefig('fig1.png', bbox_inches='tight')
