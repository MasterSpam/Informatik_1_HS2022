# Python3 code to demonstrate
# Combining tuples in list of tuples
# Using list comprehension

# initializing list
test_list = [([1, 2, 3], 'gfg'), ([5, 4, 3], 'cs')]

# printing original list
print("The original list : " + str(test_list))

# Using list comprehension
# Combining tuples in list of tuples
res = [(tup1, tup2) for i, tup2 in test_list for tup1 in i]

# print result
print("The list tuple combination : " + str(res))
