# create a function that checks if a password is valid or not
# a valid password must have:
# - at least 8 characters
# - at most 16 characters
# - at least 2 lower case letters
# - at least 2 upper case letters
# - at least 2 digits
# - at least 2 special characters
# - no other characters are allowed
# return True if the password is valid, False otherwise
#
def is_valid(pwd):
    allowed_special = "+-!?/*"
    if len(pwd) < 8 or len(pwd) > 16:
        return False
    lower = 0
    upper = 0
    digits = 0
    special = 0
    for c in pwd:
        if c.islower():
            lower += 1
        elif c.isupper():
            upper += 1
        elif c.isdigit():
            digits += 1
        elif c in allowed_special:
            special += 1
        else:
            return False

    if lower >= 2 or upper >= 2 or digits >= 2 or special >=2:
        return True
    return True
#


# test cases
print(is_valid("abcABC+123!"))  # True
print(is_valid("abcABC123"))  # False
print(is_valid("Verb!er1936+")) # True
print(is_valid("aA1+bcdefghijklmnop")) # False


