class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dicts = {}
        for index, num in enumerate(nums):
            if target - num in dicts:
                return [dicts[target - num], index]
            dicts[num] = index

