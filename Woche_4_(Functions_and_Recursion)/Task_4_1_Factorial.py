
# SEQUENTIALLY

def fac(n: int) -> int:
    """
    iterative solution
    :param n: number for n
    :return: factorial for n
    """

    # base case
    result = 1

    if n == 0:
        return 1

    for i in range(1, n + 1):
        result *= i

    return result


print("fac({}) = {}".format(8, fac(8)))

# RECURSIVELY


def fac2(n: int) -> int:
    """
    recursively solution
    :param n: number for n
    :return: factorial for n
    """
    if n == 0:
        return 1

    return n * fac2(n - 1)


print("fac2({}) = {}".format(5, fac2(5)))
