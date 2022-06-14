# @param {Integer} n
# @return {Integer}
def tribonacci(n)
    a, b, c = 0, 1, 1
    return 0 if n == 0
    return 1 if n == 1
    return 1 if n == 2
    for i in 3..n
        a, b, c = b, c, a + b + c
    end
    c
end