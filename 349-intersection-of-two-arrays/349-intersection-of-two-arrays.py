class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a = nums1
        b = nums2

        a.sort()
        b.sort()
        i, j = 0, 0
        res = []
        while True:
            if i == len(a) or j == len(b):
                break
            if a[i] == b[j]:
                res.append(a[i])
                i += 1
                j += 1
                while i<len(a) and j<len(b) and a[i] == b[j] and a[i] == a[i-1]:
                    i += 1
                    j += 1
            elif a[i] > b[j]:
                j += 1
            else:
                i += 1
            # print(i, j, res)
        return res