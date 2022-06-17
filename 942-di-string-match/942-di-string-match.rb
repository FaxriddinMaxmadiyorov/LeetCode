# @param {String} s
# @return {Integer[]}
def di_string_match(s)
    res = []
    low, high = 0, s.length
    s.each_char do |char|
       if char == 'I'
           res << low
           low += 1
       else
           res << high
           high -= 1
       end
    end
    res << low
end