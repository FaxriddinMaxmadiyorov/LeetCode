class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        s = 0
        nums.sort()
        for i in range(len(nums) // 2):
            s += nums[2*i]
        return s