# @param {String[]} words
# @return {String}
def yesno(str)
    i, j = 0, str.length() - 1
    while i < j
        if str[i] == str[j]
            i += 1
            j -= 1
        else
            return false
        end
    end
    return true
end

def first_palindrome(words)
    words.each do |word|
        if yesno(word)
            return word
        end
    end
    return ""
end