def print_range(start, stop, step):
    current = start
    while current < stop:
        print(current)
        current += step

# examples
print( print_range(0, 5, 1) )
print( print_range(5, 20, 3) )
#prints
#0
#1
#2
#3
#4
#None
#5
#8
#11
#14
#17
#None