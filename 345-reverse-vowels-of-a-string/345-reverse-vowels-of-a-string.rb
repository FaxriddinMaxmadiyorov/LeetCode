# @param {String} s
# @return {String}
def reverse_vowels(s)
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    left, right = 0, s.length - 1
    while left < right
       while left < right and not vowels.include?(s[left]) 
          left += 1
       end
        
       while left < right and not vowels.include?(s[right]) 
          right -= 1
       end
        
       s[left], s[right] = s[right], s[left]
       left += 1
       right -= 1
    end
    s
end