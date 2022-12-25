# Python3 code to demonstrate working of
# Filtering uppercase characters in Tuples using for loop and if condition with list comprehension
# the functions should not return an empty tuple if the input tuple is empty or if there are no uppercase characters in the input tuple


def filter_uppercase_tuple(tup):
    return tuple(x for x in tup if x.isupper())

tup = ('A', 'b', 'C', 'd', 'E', 'f', 'G', 'h', 'I', 'j', 'K', 'l', 'M', 'n', 'O', 'p', 'Q', 'r', 'S', 't', 'U', 'v', 'W', 'x', 'Y', 'z')
print(filter_uppercase_tuple(tup))


