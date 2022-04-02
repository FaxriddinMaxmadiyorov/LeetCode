class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        for i in range(len(nums)):
            dict[target - nums[i]] = i
        for i in range(len(nums)):
            if nums[i] in dict and i != dict[nums[i]]:
                return i, dict[nums[i]]                