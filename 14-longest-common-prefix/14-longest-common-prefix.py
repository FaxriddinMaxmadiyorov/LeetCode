class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str: 
        for i in range(len(strs[0])):
            char = strs[0][i]
            for j in range(1, len(strs)):
                if len(strs[j]) > i and char == strs[j][i]:
                    continue
                else:
                    return strs[0][:i]
        return strs[0]