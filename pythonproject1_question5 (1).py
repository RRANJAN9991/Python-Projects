#This program generates a Pascal triangle until the nth row. We need to import factorial to uses the nCr method for constructing
#the Pascal triangle.
from math import *
def pascal(n):#This function will use loops generate the Pascal triangle.
    for i in range(0,n):
        for j in range(0,n-i+1):#This is the first nested loop which will be used to generate spacing to the left of the Pascal triangle.
            print(end = "   ")
        for j in range(0,i+1):#This is the second nested loop which will be used to generate the Pascal values. (Using factorials)
            new_number = factorial(i)//(factorial(j)*factorial(i-j))
            print(new_number, end = "     ")#This code is beneficial for generating spacing between Pascal values within the Pascal triangle itself.
        print()#Skips a line for each row of the Pascal triangle.
pascal(3)#These are test runs which are seperated by two lines of space each.
print()
print()
pascal(6)
print()
print()
pascal(10)
