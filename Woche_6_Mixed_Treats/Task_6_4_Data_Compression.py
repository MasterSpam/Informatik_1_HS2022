
def compress(data):
    key_tuple = ()
    value_list = []

    if not data:
        return key_tuple, value_list

    if not data[0]:
        for i in range(len(data)):
            value_list.append(())
        return key_tuple, value_list

    all_keys = sorted([*data[0]])
    key_tuple = tuple(all_keys)
    for i in range(len(data)):
        temp_value_list = []
        for key in all_keys:
            temp_value_list.append(data[i][key])
        value_list.append(tuple(temp_value_list))

    return key_tuple, value_list


data = [
    {"a": 1, "b": 2, "c": 3},
    {"a": 4, "c": 6, "b": 5}
]
print(compress(data))
