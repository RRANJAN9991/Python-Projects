#This program computes the Mandelbrot set over the range [-2,1]x[-1.5,1.5] using a
#threshold of 50. Using these parameters, the program will output an image of a
#Mandelbrot fractal.
#We import matplotlib.pyplot as it contains useful plotting tools that help with adjusting
#axis and coloring points. Importing numpy will help with creating matrices and manipulating them.
import matplotlib.pyplot as plt
import numpy


#The first function determines and returns the counter of how many iterations until
#c diverges. We will use this while plotting the points on the grid in the second function since only the bounded
#values of c will be used in the Mandelbrot set. 
def numIterations(threshold,c):
    N_max = 50
    iteration_num = 1
    z = c
    #As long as the counter (iteration_num) does not exceed the max number of iterations or absolute
    #value of z does not exceed or equal the threshold we will keep iterating.
    for iteration_num in range(1,N_max + 1):
        if (iteration_num <= N_max and abs(z) < threshold):
            z = z*z + c
            iteration_num = iteration_num + 1
        else:
            break
    return iteration_num
#This function uses the above function to generate the grid of the Mandelbrot set. The first few lines
#of code are used to set the ranges for x and y and then we use lamda to manipulate each x and y based on their ranges.
def mandelbrotPlot(threshold):
    num_points = 500
    x_range = 3.2/(num_points - 1)
    y_range =  3.2/(num_points - 1)
    plot_points = lambda x,y: ((x_range*x) - 2, (y_range*y) - 1.5)
    #We then fill in an array just to initialize it. Then using a nested for loop, we can
    #grid each coordiate into the array based on the number of iterations until c diverges for each pair. 
    mand_plot = numpy.full((num_points,num_points),0)
    for i in range(num_points):
        for j in range(num_points):
            num_iterations = numIterations(threshold, complex(*plot_points(i,j)))
            mand_plot[j][i] = num_iterations
    return mand_plot


#We will use a threshold of 50 and use matplotlib to print the grid.
mand_plot = mandelbrotPlot(50)
plt.imshow(mand_plot, extent=[-2, 1, -1.5, 1.5])
plt.gray()
plt.show()
