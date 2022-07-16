# @param {String} s
# @return {String}
def sort_sentence(s)
    s = s.split(' ')
    arr = Array.new(s.length)
    for word in s
       arr[word[word.length - 1].to_i] = word[0...word.length - 1]
    end
    arr[1..arr.length].join(' ')
end