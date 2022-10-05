s = "aB:cD"


def transform_string():

    res = s[:s.find(":")].lower() + ":" + s[s.find(":") + 1:].upper()

    return res


print(transform_string())
print()
