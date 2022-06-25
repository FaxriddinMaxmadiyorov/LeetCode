# @param {Integer[]} arr
# @return {Integer}
def peak_index_in_mountain_array(arr)
    l, r = 0, arr.length - 1
    while l < r 
       m = (l + r) / 2
       if arr[m] < arr[m + 1]
           l = m + 1
       else
           r = m
       end
    end
    return r
end