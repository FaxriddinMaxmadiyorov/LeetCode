class Solution:
    def validPalindrome(self, s: str) -> bool:
        def check(i, j):
            s1 = s[i:j]
            s2 = s[i+1:j+1]
            print(s1, s2)
            d = True
            e = True
            for k in range(len(s1) // 2):
                if s1[k] != s1[len(s1) - k - 1]:
                    d = False
            
            for k in range(len(s2) // 2):
                if s2[k] != s2[len(s2) - k - 1]:
                    e = False
            return d == True or e == True
        
        if s == s[::-1]:
            return True
        print("hjh")
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]:
                print(i, j)
                if check(i, j):
                    return True
                return False
            i += 1
            j -= 1