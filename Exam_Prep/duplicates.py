def duplicates_of(lst, xs):
    count_duplicates = 0
    for element in xs:
        count_duplicates += lst.count(element)
    return count_duplicates


assert (duplicates_of([], []) == 0)
assert (duplicates_of([1], [1]) == 1)
assert (duplicates_of([True, True], [True]) == 2)
assert (duplicates_of([1, 1, 'hello', 3], [1, 'hello', 1]) == 5)
