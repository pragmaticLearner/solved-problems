# Simple block of code to iterate through a range and get sum multiples of 3 and 5
# https://projecteuler.net/problem=1

# Using list comprehension
def sum_multiples(x):
    return sum([i for i in range(1, x) if i % 3 == 0 or i % 5 == 0])


print(sum_multiples(99999))


# Dynamic programming approach for optimal solution

def sum_multiples(y):
    Sum = 0
    for i in range(1, y):
        if i % 3 == 0 or i % 5 == 0:
            Sum += i
    return Sum


print(sum_multiples(9999999))
