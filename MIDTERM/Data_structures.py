def duplicate_every(l, n):
    counter = 1
    duplicated_list = []
    for element in l:
        duplicated_list.append(element)
        if counter % n == 0:
            duplicated_list.append(element)
        counter += 1

    return duplicated_list


print(duplicate_every([1, 3, 4, 5], 2))
print(duplicate_every([1, 4, 5, 4, 3, 2, 1], 3))
