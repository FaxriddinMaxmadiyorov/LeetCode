class Solution:
    def validPalindrome(self, s: str) -> bool:
        def check(i, j):
            s1 = s[i:j]
            s2 = s[i+1:j+1]
            return s1 == s1[::-1] or s2 == s2[::-1]
        
        if s == s[::-1]:
            return True
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]:
                if check(i, j):
                    return True
                return False
            i += 1
            j -= 1