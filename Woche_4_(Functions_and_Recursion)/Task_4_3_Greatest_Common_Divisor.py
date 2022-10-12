
def absolute_value(a):

    return abs(a)


def gcd(a, b):

    if not a and not b:
        return None

    a, b = absolute_value(a), absolute_value(b)

    if a < b:           # a needs to beginning greater than b
        a, b = b, a

    # base case
    if a == 0 or b == 0:
        return max(a, b)

    return gcd(b, a % b)


a = 26
b = 65
print(f"greatest common divisor of {a} and {b} is = {gcd(a, b)}")

