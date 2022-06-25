class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        low, up = 0, len(arr) - 1
        while low < up:
            mid = (low + up) // 2
            if arr[mid] < arr[mid + 1]:
                low = mid + 1
            else:
                up = mid

        return low
