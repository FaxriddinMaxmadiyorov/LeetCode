# @param {String} s
# @param {Integer[]} indices
# @return {String}
def restore_string(s, indices)
    res = 'a'*s.length
    i = 0
    indices.each do |index|
        res[index] = s[i]
        i += 1
    end
    res
end