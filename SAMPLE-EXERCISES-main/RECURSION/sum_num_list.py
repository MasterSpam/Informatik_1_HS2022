# recursive function to calculate the sum of a list of numbers
#

def num_list(l):
    if len(l) == 1:
        return l[0]
    else:
        return l[0] + num_list(l[1:])

l = [1,2,3,4,5,5,6]
print(num_list(l)) # prints 26

