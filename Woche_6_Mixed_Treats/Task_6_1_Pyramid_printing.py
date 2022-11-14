
h = 5


def build_string_pyramid():

    s = ""

    for i in range(1, h + 1):
        s += "*".join(str(n) for n in range(1, i + 1)) + "\n"

    for i in range(h - 1, 0, -1):
        s += "*".join(str(n) for n in range(1, i + 1)) + "\n"

    s = s[:-1]

    return s


print(build_string_pyramid())
