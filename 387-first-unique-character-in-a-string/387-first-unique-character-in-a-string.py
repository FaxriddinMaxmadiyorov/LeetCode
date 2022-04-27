class Solution:
    def firstUniqChar(self, s: str) -> int:
        a = {}
        temp = ""
        for i in range(len(s)):
            if s[i] not in a:
                a[s[i]] = 1
            else:
                a[s[i]] += 1
                

        for i in range(len(s)):
            if a[s[i]] == 1:
                return i
        return -1            
        