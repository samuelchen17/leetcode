class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """
        Loop through the array
        check if it already exists in hashmap
        if it does, return true
        if not, store num as the key in the hashmap
        return false if no duplicates are found
        """

        nums_hash = {}

        for i, num in enumerate(nums):
            if num in nums_hash:
                return "true"
            nums_hash[nums] = i
        return "false"
