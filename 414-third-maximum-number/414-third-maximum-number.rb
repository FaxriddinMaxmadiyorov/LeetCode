# @param {Integer[]} nums
# @return {Integer}
def third_max(nums)
    maximum = nums.max()
    nums_hash = Hash.new(0)
    nums.each do |ele|
       nums_hash[ele] += 1
    end
    nums.clear()
    nums_hash.each do |k, v|
        nums << k
    end
    nums.sort!
    if nums.length >= 3
        return nums[-3]
    else
        return maximum
    end
end