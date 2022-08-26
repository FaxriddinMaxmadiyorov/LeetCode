class Solution:
    def checkRecord(self, s: str) -> bool:
        a, l, max_late = 0, 0, 0
        last_day_late = False
        for ch in s:
            if ch == 'A':
                a += 1
                last_day_late = False
            elif last_day_late == False and ch == 'L':
                l = 1
                last_day_late = True
            elif last_day_late and ch == 'L':
                l += 1
            else:
                last_day_late = False
            max_late = max(l, max_late)
        print(a, max_late)
        if a < 2 and max_late < 3:
            return True
        return False
# "LALL"