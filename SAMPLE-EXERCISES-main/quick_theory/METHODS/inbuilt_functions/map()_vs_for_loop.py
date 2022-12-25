# function to square a given number
def squareNum(a):
    return a * a


listnum = [0, -1, 3, 4.5, 99, .08]

# using 'map' to call the function
# 'squareNum' for all the elements
# of 'listnum'
x = map(squareNum, listnum) #map(function, iterableObject)

# map function returns a map
# object at this particular
# location
print(x) # <map object at 0x10b7f2080>

# convert map to list
print(list(x))

# alternate way to square all
# elements of 'listnum' using
# 'for loop'

for i in listnum:
    square = i * i
    print(square)