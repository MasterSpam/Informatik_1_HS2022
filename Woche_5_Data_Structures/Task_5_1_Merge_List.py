
def merge(a, b):
    merge_list = []

    if not a or not b:
        return merge_list

    if len(a) > len(b):                     # extended smaller lists without repeating last element
        for i in range(len(a) - len(b)):
            b.append(b[-1])
    elif len(a) < len(b):
        for i in range(len(b) - len(a)):
            a.append(a[-1])

    return list(zip(a, b))


print(merge([0, 1, 2], [5, 6]))
