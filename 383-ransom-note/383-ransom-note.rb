# @param {String} ransom_note
# @param {String} magazine
# @return {Boolean}
def can_construct(ransom_note, magazine)
    h = Hash.new(0)
    magazine.each_char do |char|
        h[char] += 1
    end
    ransom_note.each_char do |char|
        h[char] -= 1
    end
    h.each do |key, value|
       return false if value < 0 
    end
    return true
end