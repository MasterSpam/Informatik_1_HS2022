def print_range(start, stop, step):
    number = 0
    while number < stop:
        if start + number < stop:
            print(start + number)
        number += step


print(print_range(0, 5, 1))
print(print_range(5, 20, 3))
