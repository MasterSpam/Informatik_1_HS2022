def unique_names(names1, names2):
    new_list = names1 + names2
    return list(dict.fromkeys(new_list)) # easy one line to remove duplicates from list

if __name__ == "__main__":
    names1 = ["Ava", "Emma", "Olivia"]
    names2 = ["Olivia", "Sophia", "Emma"]
    print(unique_names(names1, names2)) # should print Ava, Emma, Olivia, Sophia