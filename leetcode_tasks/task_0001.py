"""
Given an array of integers nums and an integer target, return indices of the
two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may
not use the same element twice.

You can return the answer in any order.

Constraints:

- 2 <= nums.length <= 10**4
- -10**9 <= nums[i] <= 10**9
- -10**9 <= target <= 10**9
- Only one valid answer exists.
 

Follow-up: Can you come up with an algorithm that is less than O(n2) time
complexity?
"""

from typing import Dict, List


def twoSum(nums: List[int], target: int) -> List[int]:
    nums_table: Dict[int: int] = {}
    for i in range(len(nums)):
        if target - nums[i] not in nums_table.keys():
            nums_table[nums[i]] = i
        else:
            return [nums_table[target - nums[i]], i]


nums = [162, 2, 12, 36, 121, 59, 600, 188]
target = 95

print(twoSum(nums, target))