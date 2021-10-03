"""
Algorithm for finding the largest prime factor of input number N.

Source: https://projecteuler.net/problem=3

Eg. input -> 10,        input -> 20
    output -> 5,        output -> 19

"""


def largest_prime(N):
    prime_factors = []
    if N < 2:
        return TypeError("Input number N not valid")
    else:
        flag = True
        for i in range(2, N):
            while flag:
                if N % i == 0:
                    prime_factors.append(i)
                    flag = False
        return prime_factors


print(largest_prime(3))
