from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        return indices of two numbers that add to target
        create hashmap, the key will be number, value will be index
        loop through array
        check for difference
        check if difference exists in the hashmap
        if yes, return index and value from hashmap
        if not, add to hashmap
        """
        int_map = {}
        result = []
        for i, num in enumerate(nums):
            difference = target - num
            if difference in int_map:
                return [int_map[difference], i]
            else:
                int_map[num] = i
