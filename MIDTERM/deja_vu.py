def length(iterable):
    iterable = list(iterable)
    if iterable:
        return 1 + length(iterable[1:])
    return 0


print(length([1, 2, [3, 4]]))
print(length(("a", 1, 2, None)))
print(length("oh dear"))
