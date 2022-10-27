
wa_nrs = ["0781111119", "0792653913", "0797763139", "0792793193", "0781139022", "0764320165"]


def get_possible_nrs(n):

    possible_nrs_for_juliet = []

    for i in range(2, 10):
        for j in range(10):
            possible_nr = n[:i] + str(j) + n[i:]
            print(possible_nr)
            if possible_nr in wa_nrs:
                possible_nrs_for_juliet.append(possible_nr)

    possible_nrs_for_juliet = list(set(possible_nrs_for_juliet))
    return possible_nrs_for_juliet


print(get_possible_nrs("076432165"))
