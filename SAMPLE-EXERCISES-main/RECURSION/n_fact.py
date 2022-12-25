# recursive function to calculate the factorial of a number n
#

def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * (factorial(n - 1))

print(factorial(5)) # print 120
print(factorial(10)) # print 3628800
print(factorial(20)) # print 2432902008176640000
