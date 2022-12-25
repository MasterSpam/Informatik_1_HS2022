def min_domino_rotations(top, bottom):

    for target in [top[0], bottom[0]]:

        missing_t, missing_b = 0,0

        for i,pair in enumerate(zip(top, bottom)):

            t,b = pair

            if not (t == target or b == target):
                break
            if t != target:
                missing_t +=1
            if b != target:
                missing_b +=1
            if i == len(top) - 1:
                return min(missing_t, missing_b)
    return -1


print(min_domino_rotations([2, 6, 2, 1, 2, 2], [5, 2, 4, 2, 3, 2]))
print(min_domino_rotations([3, 5, 1, 2, 6], [3, 6, 3, 3, 6]))