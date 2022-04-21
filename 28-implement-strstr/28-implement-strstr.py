class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i, j = 0, 0
        while j < len(needle) and i < len(haystack): 
            if haystack[i] == needle[j]:
                j += 1
            else:
                i = i - j
                j = 0
            i += 1
            
        return i - j if j == len(needle) else -1