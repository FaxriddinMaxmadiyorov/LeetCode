# @param {String} moves
# @return {Boolean}
def judge_circle(moves)
    ver, hor = 0, 0
    moves.each_char do |move|
        if move == 'R'
            hor += 1
        elsif move == 'L'
            hor -= 1
        elsif move == 'U'
            ver += 1
        elsif move == 'D'
            ver -= 1
        end
    end
    return true if ver == 0 and hor == 0
    return false
end
