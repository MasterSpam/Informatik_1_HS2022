def multiples_of(n, count):
    my_dict = {}

    if count < 0 or not isinstance(count, int):
        return False

    for i in range(1, count + 1):
        my_dict[i] = n * i

    return my_dict


assert (multiples_of(3, 4) == {1: 3, 2: 6, 3: 9, 4: 12})
assert (multiples_of(2, 0) == {})
assert (multiples_of(0, 3) == {1: 0, 2: 0, 3: 0})
assert (multiples_of(-2, 3) == {1: -2, 2: -4, 3: -6})
