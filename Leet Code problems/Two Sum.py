"""
Algorithm to find two indeces given they sum to a target integer.

Source: https://leetcode.com/problems/two-sum/

"""


def twoSum(nums, target):
    values = dict()

    for i, elem in enumerate(nums):
        comp = target - elem

        if comp in values:
            return [values[comp], i]

        values[elem] = i
    return []


print(twoSum([1, 2, 3], 4))
