#!/usr/bin/env python
# coding: utf-8

import pandas as pd
from statistics import variance

from matplotlib.pyplot import subplot, scatter, plot, axis
from scipy.stats import linregress

dataf = pd.read_excel('Anscombe Dataset.xls')

# Calculate Mean of x for each dataset 
print('________________________Mean of x_____________________________')
print('x1 : {0:.3f}'.format(sum(dataf['x1'])/11), 
      '\tx2 : {0:.3f}'.format(sum(dataf['x2'])/11), 
      '\tx3 : {0:.3f}'.format(sum(dataf['x3'])/11), 
      '\tx4 : {0:.3f}'.format(sum(dataf['x4'])/11))

# Calculate Mean of y for each dataset 
print('\n________________________Mean of y_____________________________')
print('y1 : {0:.3f}'.format(sum(dataf['y1'])/11), 
      '\ty2 : {0:.3f}'.format(sum(dataf['y2'])/11), 
      '\ty3 : {0:.3f}'.format(sum(dataf['y3'])/11), 
      '\ty4 : {0:.3f}'.format(sum(dataf['y4'])/11))

# Calculate Variance of x for each dataset 
print('\n______________________Variance of x___________________________')
print('x1 : {0:.3f}'.format(variance(dataf['x1'])), 
      '\tx2 : {0:.3f}'.format(variance(dataf['x2'])), 
      '\tx3 : {0:.3f}'.format(variance(dataf['x3'])), 
      '\tx4 : {0:.3f}'.format(variance(dataf['x4'])))

# Calculate Variance of y for each dataset 
print('\n______________________Variance of y___________________________')
print('y1 : {0:.3f}'.format(variance(dataf['y1'])), 
      '\ty2 : {0:.3f}'.format(variance(dataf['y2'])), 
      '\ty3 : {0:.3f}'.format(variance(dataf['y3'])), 
      '\ty4 : {0:.3f}'.format(variance(dataf['y4'])))

# Calculate Coorelation of x & y for each dataset 
print('\n__________________Correlation of x & y________________________')
print('x1/y1 : {0:.3f}'.format(dataf['x1'].corr(dataf['y1'])),
      '\tx2/y2 : {0:.3f}'.format(dataf['x2'].corr(dataf['y2'])),
      '\tx3/y3 : {0:.3f}'.format(dataf['x3'].corr(dataf['y3'])),
      '\tx4/y4 : {0:.3f}'.format(dataf['x4'].corr(dataf['y4'])))

xmax = 20
ymax = 14

#plot graph of 1st dataset
ax1 = subplot(2, 2, 1)
scatter(dataf['x1'], dataf['y1'])
slope, intercept, r_value, p_value, std_err = linregress(dataf['x1'], dataf['y1'])
plot([0, xmax], [intercept, slope * xmax + intercept])

#plot graph of 2nd dataset
subplot(2, 2, 2, sharex=ax1, sharey=ax1)
scatter(dataf['x2'], dataf['y2'])
slope, intercept, r_value, p_value, std_err = linregress(dataf['x2'], dataf['y2'])
plot([0, xmax], [intercept, slope * xmax + intercept])

#plot graph of 3rd dataset
subplot(2, 2, 3, sharex=ax1, sharey=ax1)
scatter(dataf['x3'], dataf['y3'])
slope, intercept, r_value, p_value, std_err = linregress(dataf['x3'], dataf['y3'])
plot([0, xmax], [intercept, slope * xmax + intercept])

#plot graph of 4th dataset
subplot(2, 2, 4, sharex=ax1, sharey=ax1)
scatter(dataf['x4'], dataf['y4'])
slope, intercept, r_value, p_value, std_err = linregress(dataf['x4'], dataf['y4'])
plot([0, xmax], [intercept, slope * xmax + intercept])
