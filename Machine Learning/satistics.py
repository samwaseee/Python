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

x = np.std(speed)
print("Standard Deviation:", x)

# Variance
x = np.var(speed)
print("Variance:", x)
print("standard Deviation using variance:", np.sqrt(x))
# Range
x = np.ptp(speed)
print("Range:", x)