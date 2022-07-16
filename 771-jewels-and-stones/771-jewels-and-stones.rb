# @param {String} jewels
# @param {String} stones
# @return {Integer}
require 'set'

def num_jewels_in_stones(jewels, stones)
    hash = Hash.new()
    jewels.each_char do |jewel|
       hash[jewel] = 1 
    end
    cnt = 0
    
    stones.each_char do |char|
        if hash[char] == 1
            cnt += 1    
        end
    end
    cnt
end