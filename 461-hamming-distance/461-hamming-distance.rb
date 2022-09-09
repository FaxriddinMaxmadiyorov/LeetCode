# @param {Integer} x
# @param {Integer} y
# @return {Integer}
def hamming_distance(x, y)
    res, cnt = (x ^ y).to_s(2), 0
    res.each_char do |i|
        if i == '1'
            cnt += 1
        end
    end
    cnt
end