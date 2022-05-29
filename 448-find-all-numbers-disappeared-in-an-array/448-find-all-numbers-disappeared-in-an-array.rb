# @param {Integer[]} nums
# @return {Integer[]}
def find_disappeared_numbers(nums)
    hash = Hash.new(0)
    for i in nums
        hash[i] += 1
    end
    res = []
    for i in (1..nums.length)
       if hash[i] == 0
           res << i
       end
    end
    return res
end