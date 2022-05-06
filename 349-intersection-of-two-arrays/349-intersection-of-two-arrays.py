class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = set()
        h = {}
        for i in nums1:
            h[i] = 0
        for i in nums2:
            if i in h:
                res.add(i)
                
        return res