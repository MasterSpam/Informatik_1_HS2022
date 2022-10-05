
import re
pwd = "ab12+/AB"

#   8-16 Characters
#   a-z, A-Z, "+", "-", "*", "/"
#   at least 2 of each of these


def is_valid():

    validity = True

    if len(pwd) < 8 or len(pwd) > 16:
        validity = False
    elif re.search(r'^[A-Za-z0-9*/+-]+$', pwd) is None:
        validity = False
    elif sum(1 for c in pwd if c.isupper()) < 2 or sum(1 for c in pwd if c.islower()) < 2 \
            or sum(1 for c in pwd if c.isdigit()) < 2 or len(re.findall('[*/+-]', pwd)) < 2:
        validity = False

    return validity


print(is_valid())
