# # @param {String} s
# # @param {String} t
# # @return {Boolean}
def is_anagram(s, t)
  ss = Hash.new(0)
   
  s.each_char do |i|
        ss[i] += 1    
  end
   
  t.each_char do |i|
        ss[i] -= 1    
  end
  ss.each do |key, value|
     if value != 0
        return false 
     end
  end
return true
end
is_anagram("jh", "klsdkf")
# s = "huyuy"
# s.each_char do |char|
#     puts char
# end