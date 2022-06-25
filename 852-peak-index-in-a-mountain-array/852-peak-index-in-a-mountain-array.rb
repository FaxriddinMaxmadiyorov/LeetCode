# @param {Integer[]} arr
# @return {Integer}
def peak_index_in_mountain_array(arr)
    i = 0
    while arr[i] < arr[i + 1]
        i += 1
    end
    return i
end