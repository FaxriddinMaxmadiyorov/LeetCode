# @param {Integer} n
# @return {Integer}
def arrange_coins(n)
    d = Math.sqrt(1 + 8 * n)
    return ((d - 1) / 2).to_i
end