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
