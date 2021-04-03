from itertools import combinations
from numpy import prod


def sub_seq_prodSum(a, m):
    array = list(combinations(a, m))
    prod_perRow = []

    for i in array:
        if not array:
            return None
        else:
            prod_perRow.append(prod(i))
            return sum(prod_perRow)


print(sub_seq_prodSum([], 2))

