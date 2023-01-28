'''
You are given a positive integer array nums.

 - The element sum is the sum of all the elements in nums.
 - The digit sum is the sum of all the digits (not necessarily distinct) that appear in nums.
Return the absolute difference between the element sum and digit sum of nums.

Note that the absolute difference between two integers x and y is defined as |x - y|.

1 <= nums.length <= 2000
1 <= nums[i] <= 2000
'''
from typing import List


def differenceOfSum( nums: List[int]) -> int:
    first_sum: int = 0
    second_sum: int = 0
    for num in nums:
        first_sum += num
    
    nums_str = ''.join(list(map(str, nums)))
    for digit in nums_str:
        second_sum += int(digit)
    
    diff: int = first_sum - second_sum
    return abs(diff)
            

a = [1,15,6,3]


print(differenceOfSum(a))  # 9