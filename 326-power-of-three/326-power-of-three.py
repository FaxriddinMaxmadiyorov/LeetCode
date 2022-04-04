class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        def find_ternary(num):  #2
            quotient = num/3    #3
            remainder = num%3
            if quotient == 0:   #4
                return ""
            else:
                return find_ternary(int(quotient)) + str(int(remainder)) 
        cnt, cn = 0, 0
        nn = find_ternary(n)
        print(nn)
        if n > 0:
            for i in nn:
                if i == '1':
                    cnt += 1
                elif i == '0':
                    cn += 1
            # print(cnt, cn)
            return cnt == 1 and cnt + cn == len(nn)
        else:
            return False