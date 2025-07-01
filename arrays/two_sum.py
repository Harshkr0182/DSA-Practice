# Leetcode Two Sum Problem
# Time Complexity: O(n)

def two_sum(nums, target):
    map = {}
    for i, num in enumerate(nums):
        if target - num in map:
            return [map[target - num], i]
        map[num] = i
