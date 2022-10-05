
from math import sqrt, ceil
n = 0


def sieve_of_eratosthenes():

    my_list = list(range(2, n + 1))
    temp_list = list(range(2, n + 1))
    primes_up_to_n = []

    for element in my_list:
        if element in temp_list:
            primes_up_to_n.append(element)
            for my_num in temp_list:
                if my_num % element == 0:
                    temp_list.remove(my_num)

    if len(primes_up_to_n) == 0:
        primes_up_to_n = ["empty"]

    return primes_up_to_n


print(sieve_of_eratosthenes())