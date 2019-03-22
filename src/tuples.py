"""
Python tuples are sort of like lists, except they're immutable and
are usually used to hold heterogenous data, as opposed to lists
which are typically used to hold homogenous data. Tuples use 
parens instead of square brackets. 

More specifically, tuples are faster than lists. If you're looking
to just define a constant set of values and that set of values 
never needs to be mutated, use a tuple instead of a list. 

Additionally, your code will be safer if you opt to "write-protect"
data that does not need to be changed. Tuples enforce immutability
automatically. 
"""

# Example:

import math

def dist(a, b):
    """Compute the distance between two x,y points."""
    x0, y0 = a  # Destructuring assignment
    x1, y1 = b
    
    return math.sqrt((x1 - x0)**2 + (y1 - y0)**2)

a = (2, 7)   # <-- x,y coordinates stored in tuples
b = (-14, 72)

# Prints "Distance is 66.94"
print("Distance is: {:.2f}".format(dist(a, b)))



# Write a function `print_tuple` that prints all the values in a tuple

# YOUR CODE HERE

def print_tuple(t):
    if type (t) is not tuple: #beak if we dont get the value we expected
        print(t);
    else:
        for a in enumerate(t):
            print(a);
        
t = (1, 2, 5, 7, 99)
print_tuple(t)  # Prints 1 2 5 7 99, one per line

#below will also work because of the function over runing the stack
#Python is a run time language so when you redeclare something on the stack
#the object is over written for all the folling code, since this code flows
#from top to bottom defining it below the last function will creat a new
#funciton pointer in the vm that over rides the old function pointer and so
#this new function will be call for all remaining code.

#def print_tuple(t):
    #print(t);


# Declare a tuple of 1 element then print it
u = (1)  # What needs to be added to make this work?
#the above is not a tuple.
#to make it a tuple you must
#u = (1,) #this is the only way to make a one element tuple

print_tuple(u)
