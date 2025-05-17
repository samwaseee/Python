import matplotlib.pyplot as plt
from scipy import stats

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

slope, intercept, r, p, std_err = stats.linregress(x, y)
'''
slope: how steep the line is.

intercept: where the line crosses the y-axis.

r: correlation coefficient (how well the line fits the data; closer to ±1 means better fit).

p: p-value (used to test the hypothesis that the slope is zero).

std_err: standard error of the estimated slope.
'''

def myfunc(x):
  return slope * x + intercept        # y = mx + b
    
mymodel = list(map(myfunc, x))     # list(map(function, iterable)) applies the function to all items in the iterable

speed = myfunc(10)

plt.scatter(x, y)
plt.plot(x, mymodel)      # plot the line
plt.plot([10, 10], [speed, 75], color = 'y', alpha= 0.5)   # plot a point at (10, speed)
plt.plot([0, 10], [speed, speed], color = 'y', alpha = 0.5 )   # plot a point at (10, speed)
plt.show() 