class Solution:
    def firstUniqChar(self, s: str) -> int:
        a = collections.Counter(s)
        # return a       

        for i in range(len(s)):
            if a[s[i]] == 1:
                return i
        return -1            
        