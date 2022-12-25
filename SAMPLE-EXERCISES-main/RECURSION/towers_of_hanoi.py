# create a function that prints the steps required to solve the Towers of Hanoi problem for a given number of disks using recursion

def req_steps(num_disks):
    if num_disks == 1:
        return 1
    return 2 * req_steps(num_disks - 1) + 1

num_disks = 3
print(req_steps(num_disks)) # prints 7
num_disks = 4
print(req_steps(num_disks)) # prints 15
