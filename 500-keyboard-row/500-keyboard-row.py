class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        s1 = set("qwertyuiop")
        s2 = set("asdfghjkl")
        s3 = set("zxcvbnm")
        res = []
        for word in words:
            w = set(word.lower())
            if w <= s1 or w <= s2 or w <= s3:
                res.append(word)
        return res