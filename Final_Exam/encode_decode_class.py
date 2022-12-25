
def encode(input_string, ceaser_shift, censor):
    encoded = ""
    for index, char in enumerate(input_string):
        encoded += chr(ord(char) + ceaser_shift) + chr(censor[index % len(censor)])
    return encoded


def decode(input_string, ceaser_shift, censor):
    pass


print(encode("hello", 3, [65,99,120]) ==
     ([107, 104, 111, 111, 114], [107, 65, 104, 99, 111, 120, 111, 65, 114, 99], 'kAhcoxoArc'))
print(decode("kAhcoxoArc", 3, [65,99,120]) ==
     ([107, 65, 104, 99, 111, 120, 111, 65, 114, 99], [107, 104, 111, 111, 114], 'hello'))
