def all_falsy(values):

    for element in values:
        if element:
            return False
    return True


assert all_falsy([False, "", 0, []])
assert (not all_falsy([False, "no", 0.1]))
assert all_falsy([[]])
