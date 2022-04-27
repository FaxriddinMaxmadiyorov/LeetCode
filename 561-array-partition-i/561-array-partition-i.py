class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        s = 0
        nums.sort()
        for i in range(len(nums) // 2):
            s += min(nums[2 * i], nums[2 * i + 1])
        return s