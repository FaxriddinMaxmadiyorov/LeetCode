# # @param {String} s
# # @param {String} t
# # @return {Boolean}
def is_anagram(s, t)
  ss = Hash.new(0)
  tt = Hash.new(0)
   
  s.each_char do |i|
        ss[i] += 1    
  end
   
  t.each_char do |i|
        tt[i] += 1    
  end
   
  ss.each do |key, value|
    if ss[key] != tt[key]
        return false  
    end
  end
    tt.each do |key, value|
    if ss[key] != tt[key]
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