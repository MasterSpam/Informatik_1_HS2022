def is_valid_encoding(a, b, mapping):
    if a == b:
        if not a and not b:
            return True
    else:
        if not a and not b:
            return False

    encoded = ""
    for char in a:
        if char in mapping:
            encoded += mapping[char]

    return encoded == b


assert (is_valid_encoding(None, None, {}))
assert (is_valid_encoding(None, None, {'i': "don't care"}))
assert (not is_valid_encoding(None, '', {}))
assert (not is_valid_encoding('', None, {}))
assert (is_valid_encoding('cat', 'dog', {'c': 'd', 'a': 'o', 't': 'g'}))
assert (is_valid_encoding('a', 'archer', {'a': 'archer'}))
assert (is_valid_encoding('no', 'yes', {'n': 'y', 'o': 'es', 'z': 'z'}))
