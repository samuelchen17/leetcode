class Solution:
    def twoSum(self, nums, target: int):
        numsSorted = nums.copy()
        numsSorted.sort()
        result = []
        print(numsSorted)
        p1 = 0
        p2 = len(numsSorted) - 1
        while p1 < p2:
            if (numsSorted[p1] + numsSorted[p2]) > target:
                p2 -= 1
            elif (numsSorted[p1] + numsSorted[p2]) < target:
                p1 += 1
            else:
                x = numsSorted[p1]
                y = numsSorted[p2]
                for i in range(0, len(nums)):
                    if nums[i] == x:
                        result.append(i)
                    elif nums[i] == y:
                        result.append(i)
                break

        return result


# too slow due to nested while loops
def twoSumNest(nums, target):
    """
    create 2 pointers
    p1 points at start
    p2 points at end
    while p1 is less than len(nums) - 2
    check if value of p1 + p2 = target
    if true
    return p1 and p2
    if not, p2--
    if p2 == p1, p1++
    """
    result = []
    p1 = 0

    while p1 < len(nums) - 1:
        p2 = len(nums) - 1
        while p2 != p1:
            if target == nums[p1] + nums[p2]:
                result = [p1, p2]
                return result
            else:
                p2 -= 1
        p1 += 1
