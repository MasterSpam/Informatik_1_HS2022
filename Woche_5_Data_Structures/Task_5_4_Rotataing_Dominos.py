
def min_domino_rotations(top, bottom):

    selected_number = -1
    num_switches_top = 0
    num_switches_bottom = 0

    for i in range(7):   # check whether any number is in all tokens
        counter = 0

        for num_pair in zip(top, bottom):
            if i not in num_pair:
                break
            counter += 1

        if counter == len(top):    # means that this number is ours potential target
            selected_number = i

    if selected_number == -1:   # no Number is possible
        return -1

    for j in range(len(top)):
        if top[j] != selected_number:
            num_switches_top += 1

    for j in range(len(top)):
        if bottom[j] != selected_number:
            num_switches_bottom += 1

    return min(num_switches_top, num_switches_bottom)


print(min_domino_rotations([2, 6, 2, 1, 2, 2],
                           [5, 2, 4, 2, 3, 2]))

print(min_domino_rotations([3, 5, 1, 2, 6],
                           [3, 6, 3, 3, 6]))

print(min_domino_rotations([2, 2, 2, 1, 2, 2],
                           [5, 6, 4, 2, 3, 2]))

print(min_domino_rotations([3, 3, 1, 2, 3],
                           [3, 6, 3, 3, 5]))

print(min_domino_rotations([5, 2, 4, 2, 3, 2],
                           [2, 6, 2, 1, 2, 2]))

