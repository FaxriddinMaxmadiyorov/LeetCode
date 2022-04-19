class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minLen = 10000000000000000000000000000
        for i in strs:
            minLen = min(minLen, len(i))
            
        low, high = 1, minLen
        
        while low <= high:
            mid = (low + high) // 2
            if self.isCommonPref(strs, mid):
                low = mid + 1
            else:
                high = mid - 1
        return strs[0][:(low + high) // 2]
    
    def isCommonPref(self, strs, size):
        s0 = strs[0][:size]
        for i in range(1, len(strs)):
            if strs[i][:size] != s0:
                return False
        return True