#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 19:57:53 2019

@author: manzars
"""

# using lambda for returning square(x)
y = lambda x: x**2
y(2) #will return 4

#passing multiple value to lambda for evaluting x^2 + 2y + 3
z = lambda x, y: x**2 + 2*y + 3
z(2,3) #will return 13



# Using Map function to iterate through some function
def makeOdd(x):
    return x*2 + 1
x = map(makeOdd, [2,4,6])
list(x) #this will return list of [5,9,13] here lenth of input is always equal to length of output

#using lambda with map function
x = map(lambda x, y: x + y, [10,20,30], [40,50,60])
list(x) # will return list of [50, 70, 90]



#using filter function to filter the values of any data type. Here the length of input and output may or may not same
def fil(x):
    return (x%2 != 0)
x = filter(fil, [1,2,3,4,5])
list(x) #this will return list of [1, 3, 5]

#using lambda with filter
x = filter(lambda x: (x%2 != 0), [1,2,3,4,5])
list(x)



#using Reduce Function for reducing the output. It takes n input but return only 1 output 
from functools import reduce
def summ(x, y):
    return x + y
x = reduce(summ, [1,2,3,4,5])
x # will return sum of every element of that list

#using lambda with reduce
y = reduce(lambda x,y: x+y, [1,2,3,4])
y #will return only one value that is 10



#Using Zip function to make iterable object 
x = [1,2,3,4,5]
y = ("one","two","three","four","five")
z = zip(x,y)
list(z) # will return [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'), (5, 'five')]

# zip function take sequence of input i;e def zip(*args) which take no keyworded sequence of parameter
x = [1,2,3,4,5]
y = ("one","two","three","four","five")
p = ["ek","do","teen","char","paanch"]
z = zip(x,y,p)
list(z)# will return [(1,"one","ek"),(),(),(),()] and so on

# zip function can unzip also
x, y, p = zip(*z) # this will return 3 list of which we provide earlier



#some Important parameter types are (*args) and (**kwargs)
# only onne astrisk mark i used for passing non keyworded sequence of parameter
# double astrisk mark is used for passing keyworded sequence of parameter

#example of (*args)
def rand(*args):
    for i in args:
        print(i)
rand("one","two",3,4) # this will print every input we pass to rand() function

# Exmple of (**kwargs)
def rand(**kwargs):
    for key, value in kwargs.items():
        print("key = %s, value = %s"%(key,value))
rand(one = 1, two = 2, three = 3) # will return expected value