#!/usr/bin/env python3

# elegant, high-level solution
def min_domino_rotations(top, bottom):
    # for any x between 1 and 7
    for x in range(1, 7):
        # if x appears in ALL pairs (of top and bottom numbers)
        if all(x in d for d in zip(top, bottom)):
            # compute the maximum number of switches necessary to achieve this
            return len(top) - max(top.count(x), bottom.count(x))
    return -1

# more procedural solution
import itertools
def _min_domino_rotations(top, bottom):

    # get all possible choices for flipping a domino or not
    # (put this expression into the python shell to see what it produces)
    permutations = ["".join(seq) for seq in itertools.product("01", repeat=len(top))]

    # keep track of how many flips are necessary to get a row of equal values
    all_equal = []

    # go through all permutations
    for perm in permutations:
        # for creating switched variants
        top_applied = []
        bot_applied = []
        # keep track of how many switches were applied
        switched = 0
        # apply permutation of domino or not for each index
        for index in range(len(top)):
            if perm[index] == "1":
                switched += 1
                top_applied.append(bottom[index])
                bot_applied.append(top[index])
            else:
                top_applied.append(top[index])
                bot_applied.append(bottom[index])

        # check if top or bottom row contains all equal values
        equal = len(set(top_applied)) == 1 or len(set(bot_applied)) == 1

        # if it worked, put number of applied switches into overall statistic
        if equal: all_equal.append(switched)

    # if nothing worked (all_equal is empty)
    if all_equal == []: return -1
    # otherwise, return lowest number of possible switches:
    return min(all_equal)

# test cases
print(min_domino_rotations([2, 6, 2, 1, 2, 2], [5, 2, 4, 2, 3, 2]))
print(min_domino_rotations([3, 5, 1, 2, 6], [3, 6, 3, 3, 6]))
