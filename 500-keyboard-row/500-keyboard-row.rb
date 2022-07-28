# @param {String[]} words
# @return {String[]}
def find_words(words)
    res = Array.new
    s1 = "qwertyuiop"
    s2 = "asdfghjkl"
    s3 = "zxcvbnm"
    h = Hash.new
    s1.each_char do |ch|
        h[ch] = 1 
    end
    s2.each_char do |ch|
        h[ch] = 2 
    end
    s3.each_char do |ch|
        h[ch] = 3 
    end
    words.each do |word|
        number = h[word[0].downcase]
        done = true
       word.each_char do |ch|
           if number != h[ch.downcase]
              done = false
               break 
           end
       end
        if done
           res << word 
        end
    end
    res
end