# @param {String[]} ops
# @return {Integer}
def cal_points(ops)
    stack = Array.new
    for op in ops
        if op == '+'
            stack << stack[-1] + stack[-2]
        elsif op == 'C'
            stack.pop()
        elsif op == 'D'
            stack << 2 * stack[-1]
        else
            stack << op.to_i
        end
    end
    stack.sum()
end