#-------------------------------------------------------------------------------
# Name:        LinearRegression.py
# Purpose:     Calculates a linear regression model and plots the data
# Author:      Kyle T. Peterson
#              Saint Louis University
#              Center for Sustainability
# Created:     09/03/2017
#-------------------------------------------------------------------------------

# Import Modules
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np

# define input files
WQdata= r"E:\WQ_Research\Regression\Chl_Oct28.txt"
SpecData= r"E:\WQ_Research\Regression\SpecOct28.txt"

# Read in data as arrays
x = np.genfromtxt(WQdata, dtype='float',delimiter='tab')
y = np.genfromtxt(SpecData, dtype='float',delimiter='tab')

# Fit the model
slope, intercept, r_value, p_value, slope_std_error = stats.linregress(x, y)

# Calculate outputs
predict_y = intercept + slope * x
pred_error = y - predict_y
degrees_of_freedom = len(x) - 2
residual_std_error = np.sqrt(np.sum(pred_error**2) / degrees_of_freedom)

# Create Plot
plt.plot(x, y, 'o', label='original data')
plt.plot(x, intercept + slope*x, 'r', label='fitted line')
plt.legend()
plt.show()
