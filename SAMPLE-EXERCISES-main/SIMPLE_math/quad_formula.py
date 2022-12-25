def find_roots(a, b, c):
    top1 = (-b + ((b ** 2 - 4 * a * c) ** (1 / 2)))
    top2 = (-b - ((b ** 2 - 4 * a * c) ** (1 / 2)))
    bot = (2 * a)

    if bot <= 0:
        return False
    else:
        return top1 / bot, top2 / bot


print(find_roots(2, 10, 8)) # prints (-1.0, -4.0)
print(find_roots(1, 2, -3)) # prints (1.0, -3.0)
print(find_roots(2, 4, 2)) # prints (-1.0, -1.0)

