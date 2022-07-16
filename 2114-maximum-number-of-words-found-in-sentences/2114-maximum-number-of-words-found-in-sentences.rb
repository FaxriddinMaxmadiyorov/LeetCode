# @param {String[]} sentences
# @return {Integer}
def most_words_found(sentences)
    ans = -1
    for sentence in sentences
        cnt  = 0
       sentence.each_char do |char|
          if char == ' '
             cnt += 1
          end
       end
        ans = [cnt, ans].max
    end
    ans + 1
end