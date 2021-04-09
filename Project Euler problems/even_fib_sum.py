"""

Summing all even numbers of fibonacci sequence not exceeding 4 million

Source: https://projecteuler.net/problem=2

Algorithm approach using dynamic programming for optimal solution:

 - total = 0
 - nth fibonacci number
  - nth % 2 == 0
  - total += nth % 2

"""


def even_fib_sum(n) -> int:

    total = 0
    table = [1] * (n + 1)
    table[0], table[1] = 0, 1

    if n <= 1:
        return table[n - 1]
    else:
        for i in range(2, n+1):
            table[i] = table[i - 1] + table[i - 2]
            if table[i] % 2 == 0:
                total += table[i]
    return total


print(even_fib_sum(6))

# >>> 10
#
#