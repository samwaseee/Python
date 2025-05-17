import matplotlib.pyplot as plt
import numpy as np

# xpoints = np.array([0, 6]) # x-coordinates
# ypoints = np.array([0, 250]) # y-coordinates

# plt.plot(xpoints, ypoints) 
# plt.show()

# plt.plot(xpoints, ypoints, 'o') # Adding markers to the points
# plt.show() # Display the plot

# xpoints = np.array([1, 2, 6, 8])
# ypoints = np.array([3, 8, 1, 10])

# plt.plot(xpoints, ypoints) # Adding markers to the points
# plt.show() # Display the plot


ypoints = np.array([4,9,2,0,6])  # y-coordinates with default x-coordinates

# plt.plot(ypoints) # Adding markers to the points
# plt.show() # Display the plot

# plt.plot(ypoints, 'o:r')  # Adding markers to the points with a specific line style and color
# plt.show()  # Display the plot

# plt.plot(ypoints, 'o:r', markersize=10)  # Adding markers to the points with a specific line style and color
# plt.show()  # Display the plot

# plt.plot(ypoints, 'o:r', markersize=10, markerfacecolor='black')  # Adding markers to the points with a specific line style and color
# plt.show()  # Display the plot

# plt.plot(ypoints, marker = 'o', ms = 20, mec = 'r')
# plt.show()  # Display the plot

# plt.plot(ypoints, marker = 'o', ms = 20, mec = 'r', mew = 2)
# plt.show()  # Display the plot

# plt.plot(ypoints, marker = 'o', ms = 20, mec = 'r', mew = 2, mfc = 'black')  # Adding markers to the points with a specific line style and color
# plt.show()  # Display the plot

# plt.plot(ypoints, linestyle = 'dashed')
# plt.show()  # Display the plot

# plt.plot(ypoints, linestyle = 'dotted')
# plt.show()  # Display the plot

# plt.plot(ypoints, ':')
# plt.show()  # Display the plot

# plt.plot(ypoints, linewidth = '20.5')
# plt.show()  # Display the plot

y1 = np.array([3, 8, 1, 10])
y2 = np.array([6, 2, 7, 11])

# plt.plot(ypoints, marker = 'o', ms = 20, mec = 'r', mew = 2, mfc = 'black')  # Adding markers to the points with a specific line style and color
# plt.plot(y1, linestyle = 'dashed')
# plt.plot(y2, linestyle = 'dotted')

# plt.show()  # Display the plot

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

# font1 = {'family':'serif','color':'blue','size':20}
# font2 = {'family':'serif','color':'darkred','size':15}

# plt.title("Sports Watch Data", fontdict = font1, loc='left')
# plt.xlabel("Average Pulse", fontdict = font2)
# plt.ylabel("Calorie Burnage", fontdict = font2)

# plt.plot(x, y)
# plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)
# plt.show()

#plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

# plt.subplot(1, 2, 1) #the figure has 1 row, 2 columns, and this plot is the first plot. 
# plt.plot(x,y)

# #plot 2:
# x = np.array([0, 1, 2, 3])
# y = np.array([10, 20, 30, 40])

# plt.subplot(1, 2, 2) #the figure has 1 row, 2 columns, and this plot is the second plot. 
# plt.plot(x,y)

# plt.show()

x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

# plt.subplot(2, 1, 1)
# plt.plot(x,y)

# #plot 2:
# x = np.array([0, 1, 2, 3])
# y = np.array([10, 20, 30, 40])

# plt.subplot(2, 1, 2)
# plt.plot(x,y)

# plt.show()


#plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

# plt.subplot(1, 2, 1)
# plt.plot(x,y)
# plt.title("SALES")

# #plot 2:
# x = np.array([0, 1, 2, 3])
# y = np.array([10, 20, 30, 40])

# plt.subplot(1, 2, 2)
# plt.plot(x,y)
# plt.title("INCOME")

# plt.suptitle("MY SHOP")
# plt.show()


x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

# plt.subplot(2, 3, 1)
# plt.plot(x,y)

# x = np.array([0, 1, 2, 3])
# y = np.array([10, 20, 30, 40])

# plt.subplot(2, 3, 2)
# plt.plot(x,y)

# x = np.array([0, 1, 2, 3])
# y = np.array([3, 8, 1, 10])

# plt.subplot(2, 3, 3)
# plt.plot(x,y)

# x = np.array([0, 1, 2, 3])
# y = np.array([10, 20, 30, 40])

# plt.subplot(2, 3, 4)
# plt.plot(x,y)

# x = np.array([0, 1, 2, 3])
# y = np.array([3, 8, 1, 10])

# plt.subplot(2, 3, 5)
# plt.plot(x,y)

# x = np.array([0, 1, 2, 3])
# y = np.array([10, 20, 30, 40])

# plt.subplot(2, 3, 6)
# plt.plot(x,y)

# plt.show() 


#day one, the age and speed of 13 cars:
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])

colors = ['red', 'blue', 'green', 'yellow', 'purple', 'orange', 'pink', 'brown', 'gray', 'cyan', 'magenta', 'lime', 'navy'] 

# plt.scatter(x, y, c=colors, s=100, alpha=0.5) # c is the color of the points, s is the size of the points, alpha is the transparency

#day two, the age and speed of 15 cars:
x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])

# plt.scatter(x, y)
# plt.show()



x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
colors = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])

# plt.scatter(x, y, c=colors, cmap='viridis')
# plt.colorbar()  # Show color scale

# plt.show() 


x = np.random.randint(100, size=(100))
y = np.random.randint(100, size=(100))
colors = np.random.randint(100, size=(100))
sizes = 10 * np.random.randint(100, size=(100))
alphas = np.random.rand(100)

plt.scatter(x, y, c=colors, s=sizes, alpha=alphas, cmap='nipy_spectral')

plt.colorbar()

plt.show()