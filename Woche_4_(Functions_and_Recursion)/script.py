#!/usr/bin/env python3

import os


# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!
def absolute_value(a):
    # implement this function
    return abs(a)


# a=-19
# print(absolute_value(a))
# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!
def gcd(a, b):
    # implement this function
    # if (a and b)==0: should return none by default
    if a == 0 and b != 0:
        return absolute_value(b)
    if a != 0 and b == 0:
        return absolute_value(a)
    # if (a or b)<0:
    #     a = #invoke absolute_value(a) f(x) to return correct value of a
    #     b =  #invoke absolute_value(a) f(x)to return correct value of b
    if a > b:
        if a % b == 0:
            return absolute_value(b)
        else:
            return gcd(absolute_value(a), absolute_value(a % b))

    if a < b:
        if b % a == 0:
            return absolute_value(a)
        else:
            return gcd(absolute_value(b), absolute_value(b % a))


# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!
a = 34
b = 17
print(f"greatest common divisor of {a} and {b} is = {gcd(absolute_value(a), absolute_value(b))}")
