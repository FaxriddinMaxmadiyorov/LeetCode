class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_local, max_global = nums[0], nums[0]
        for i in range(1, len(nums)):
            max_local = max(max_local + nums[i], nums[i])
            max_global = max(max_local, max_global)
        return max_global