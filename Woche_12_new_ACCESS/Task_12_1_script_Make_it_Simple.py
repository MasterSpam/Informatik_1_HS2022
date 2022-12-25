def find_in(pairs):
    if not pairs:
        return None
    a = []
    b = pairs
    while len(b) > 1:
        for i in range(len(b)):
            if i == len(b)-1:
                break
            if b[i][1] < b[i+1][1]:
                a.append(b[i])
            else:
                a.append(b[i+1])
        if len(a) == 1:
            return a[0][0]
        b = a
        a = []
    return b[0][0]


print(find_in([('A', 1), ('B', 2), ('C', 3), ('D', 4), ('A', 1), ('B', 2)]))


def find_in_refactored(pairs):
    return min(pairs, key=lambda x: x[1])[0] if pairs else None
