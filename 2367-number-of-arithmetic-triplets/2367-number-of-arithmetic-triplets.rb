# @param {Integer[]} nums
# @param {Integer} diff
# @return {Integer}
def arithmetic_triplets(nums, diff)
    c = 0
    for num in nums
        if nums.include?(num + diff) and nums.include?(num + 2*diff)
            c += 1
        end
    end
    c
end