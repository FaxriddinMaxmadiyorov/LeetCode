def merge_alternately(word1, word2)
    i = 0
    res = String.new
    while i < word1.length || i < word2.length
        if i < word1.length
           res += word1[i]
        end
        if i < word2.length
            res += word2[i]
        end
        i += 1
    end
    return res
end