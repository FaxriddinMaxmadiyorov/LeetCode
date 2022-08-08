class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        start = '{0:0160b}'.format(start)
        goal = '{0:0160b}'.format(goal)
        c = 0
        for i in range(len(start)):
            if start[i] != goal[i]:
                c += 1
                
        return c