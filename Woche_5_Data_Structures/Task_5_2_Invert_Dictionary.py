
def invert(d):

    d_invert = {}

    for key, value in d.items():
        if value not in d_invert:
            d_invert[value] = []
        d_invert[value].append(key)
        d_invert[value].sort()

    return d_invert


# {"d": 1, "b": 1, "c": 3, 42.0: 'c', 4: 'c'}
print(invert({"a": 1, "b": 1, "c": 3}))
