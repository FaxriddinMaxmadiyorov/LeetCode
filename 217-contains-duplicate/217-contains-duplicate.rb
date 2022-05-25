# @param {Integer[]} nums
# @return {Boolean}
def contains_duplicate(nums)
    hash = Hash.new(0)
    for i in nums
        hash[i] += 1
    end
    hash.each do |key, value|
        if value > 1
            return true
        end
    end
    return false
end