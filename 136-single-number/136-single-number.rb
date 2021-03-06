# @param {Integer[]} nums
# @return {Integer}
def single_number(nums)
    res = 0
    nums.each do |i|
        res ^= i
    end
    res
end