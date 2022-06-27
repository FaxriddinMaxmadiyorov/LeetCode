# @param {String} s
# @return {Integer}
def balanced_string_split(s)
    i, res, l, r = 0, 0, 0, 0
    while i < s.length
       if s[i] == 'R'
           r += 1
       else
           l += 1 
       end
        
       if l == r
           res += 1
           l, r = 0, 0
       end
       i += 1
    end
    res
end
