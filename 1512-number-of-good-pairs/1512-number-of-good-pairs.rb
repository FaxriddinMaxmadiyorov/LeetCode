# @param {Integer[]} nums
# @return {Integer}
def num_identical_pairs(nums)
    h, s = Hash.new(0), 0
    nums.each do |e|
       h[e] += 1 
    end
    h.each do |key, value|
       if value > 1
          s += (value - 1) * value / 2 
       end
    end
    s
end