# @param {Integer} start
# @param {Integer} goal
# @return {Integer}
def min_bit_flips(start, goal)
    c = 0
    while start > 0 or goal > 0
       if start % 2 != goal % 2
           c += 1
       end
       start = start / 2
       goal = goal / 2
    end
    c
end
# 1010
# 0111