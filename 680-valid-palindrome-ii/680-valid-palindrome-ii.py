class Solution:
    def validPalindrome(self, s: str) -> bool:
        if self.check(s):
            return True
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]:
                if self.check(s[i:j]) or self.check(s[i+1:j+1]):
                    return True
                return False
            i += 1
            j -= 1
        
    def check(self, s):
        return s == s[::-1]