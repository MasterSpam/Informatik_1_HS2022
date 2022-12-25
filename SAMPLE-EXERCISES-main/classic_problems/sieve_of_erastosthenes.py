import math
# performs the Sieve of Eratosthenes algorithm and returns all primes <= n
def sieve_of_eratosthenes(n):
    if n < 2:
        return ["empty"]
    sieve_list = list(range(2, n + 1))
    temp_list = sieve_list
        # a temporary list needs to be used here because we want to avoid concurrent modifications, i.e. the
        # removal/modification of elements from the list that we loop over (this could result in elements being skipped)
        # With the introduction of list comprehensions you will soon learn about a cleaner and more elegant solution.
    for i in range(2, math.ceil(math.sqrt(n))):
        for integer in sieve_list:
            if integer % i == 0 and integer != i:
                temp_list.remove(integer)
        sieve_list = list(temp_list)
    return sieve_list

n = 100
print(sieve_of_eratosthenes(n))
# prints [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]



def where_is_waldo(lst):
    for i in range(len(lst)):
        if lst[i] == "Waldo":
            return i

print(where_is_waldo(["Alice", "Bob", "Waldo", "Winston"]))