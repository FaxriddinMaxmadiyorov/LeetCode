# @param {String} s
# @return {String}
def to_lower_case(s)
    s.length.times do |i|
        if s[i] >= 'A' and s[i] <= 'Z'
            s[i] = s[i].downcase
        end
    end
    s
end