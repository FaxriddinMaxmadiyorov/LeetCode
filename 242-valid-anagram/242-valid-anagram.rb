# @param {String} s
# @param {String} t
# @return {Boolean}
def is_anagram(s, t)
   s = s.chars.sort.join('')
   t = t.chars.sort.join('')
   s == t
end