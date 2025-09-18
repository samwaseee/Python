speed = [99, 86, 87, 88, 100, 86, 87, 88, 100, 86, 87, 88, 100]
# Mean
mean = sum(speed) / len(speed)
# print("Mean:", mean)

import numpy as np

x = np.mean(speed)
# print("Mean using numpy:", x)

# Median

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

median = np.median(speed)
# print("Median:", median)

# Mode
# from scipy import stats     

# x = stats.mode(speed)
# print("Mode:", x)
# print("Mode value:", x.mode)
# print("Mode count:", x.count)

# Standard Deviation
'''Standard deviation is a number that describes how spread out the values are.

A low standard deviation means that most of the numbers are close to the mean (average) value.

A high standard deviation means that the values are spread out over a wider range.

Example: This time we have registered the speed of 7 cars:

speed = [86,87,88,86,87,85,86]

The standard deviation is:

0.9

Meaning that most of the values are within the range of 0.9 from the mean value, which is 86.4.
'''

x = np.std(speed)
# print("Standard Deviation:", x)   

# Variance
'''Variance is a number that describes how far a set of numbers are spread out from their average value.
The variance is the average of the squared differences from the Mean.'''

x = np.var(speed)                  
# print("Variance:", x)
# print("standard Deviation using variance:", np.sqrt(x))

# Range
'''The range is the difference between the highest and lowest values in a set of data.'''
x = np.ptp(speed)
print("Range:", x)

ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31] 

x = np.percentile(ages, 75)
print("75% people are "+ str(x) + " years old or younger.")