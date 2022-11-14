def apply(f, values):
    my_list = []
    for element in values:
        my_list.append(f(element))
    return my_list


print(apply(max, [[1, 2], [4.5, 1, 3]]))
print(apply(lambda x: x.upper(), ["hello", "world"]))
