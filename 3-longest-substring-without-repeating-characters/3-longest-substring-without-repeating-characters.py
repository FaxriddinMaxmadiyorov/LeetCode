class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dict = {}
        used= []
        i, mini, cnt = 0, 0, 0
        if len(s) == 0:
            return 0
        while True:
            if s[i] in used:
                mini = max(mini, cnt)
                cnt = 0
                temp = i
                i = dict[s[i]]
                dict[s[i]] = temp
                used.clear()
            else:
                cnt += 1
                used.append(s[i])
                dict[s[i]] = i
            if i == len(s) - 1:
                break
            else:
                i += 1
        return max(mini, cnt)