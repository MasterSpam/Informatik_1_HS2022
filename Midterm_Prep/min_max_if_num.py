def min_max_of(values):
    my_min = None
    my_max = None
    if values is None:
        return my_min, my_max

    for element in values if values else []:
        if isinstance(element, (int, float)) and not isinstance(element, bool):
            if not my_min or element < my_min:
                my_min = element
            if not my_max or element > my_max:
                my_max = element

            # my_min = element if not my_min or element < my_min else my_min
            # my_max = element if not my_max or element > my_max else my_max
    if my_min == my_max:
        my_max = None
    return my_min, my_max


assert (min_max_of(None) == (None, None))
assert (min_max_of([]) == (None, None))
assert (min_max_of([True]) == (None, None))
assert (min_max_of([0, 0.0]) == (0, None))
assert (min_max_of([0, 0.0]) == (0.0, None))
assert (min_max_of([-1, 0, 1]) == (-1, 1))
assert (min_max_of(['a', 'A', 1]) == (1, None))
