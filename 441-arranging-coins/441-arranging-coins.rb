# @param {Integer} n
# @return {Integer}
def arrange_coins(n)
    t = 1
    while n > 0
       if n - t >= 0
          n -= t
          t += 1
       else
           break
       end
    end
    return t - 1
end