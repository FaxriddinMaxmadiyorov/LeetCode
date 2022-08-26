class Solution:
    def checkRecord(self, s: str) -> bool:
        a, l, max_late = 0, 0, 0
        last_day_late = False
        for ch in s:
            if ch == 'L':
                if last_day_late:
                    l += 1
                    max_late = max(max_late, l)
                else:
                    l = 1
                    last_day_late = True
            else:
                last_day_late = False
                if ch == 'A':
                    a += 1
                        
        print(a, max_late)
        if a < 2 and max_late < 3:
            return True
        return False