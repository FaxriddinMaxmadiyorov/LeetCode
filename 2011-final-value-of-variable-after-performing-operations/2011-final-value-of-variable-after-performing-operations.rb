# @param {String[]} operations
# @return {Integer}
def final_value_after_operations(operations)
    x = 0
    for oper in operations
       if oper[0] == '+' || oper[1] == '+'
          x += 1
        else
           x -= 1
       end
    end
    x
end