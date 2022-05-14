# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        i, j =1, n
        while i < j:
            x=guess((i+j)//2)
            if x ==-1:
                j=(i+j)//2-1
            if x==1:
                i=(i+j)//2+1
            if x==0:
                return (i+j)//2
        return (i+j)//2