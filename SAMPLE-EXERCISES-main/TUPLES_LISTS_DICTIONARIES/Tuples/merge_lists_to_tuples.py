def merge(a, b):
    mergelist = [] # create empty list
    for i in range(max((len(a), len(b)))):

        # takes element of a and b at same index WHILE same index IS TRUE.
        while True:
            try:
                tup = (a[i], b[i])

            except IndexError:
            # if index != same i.e len(a) != len(b) then:
                if len(a) > len(b):
                    b.append(b[-1]) # append last element of b if a is longer
                    tup = (a[i], b[i])
                elif len(a) < len(b):
                    a.append(a[-1]) # append last element of a if b is longer
                    tup = (a[i], b[i])
                continue

            mergelist.append(tup) # append tuples to empty list
            break
    return mergelist


