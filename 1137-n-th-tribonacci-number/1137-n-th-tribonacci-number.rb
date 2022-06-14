# @param {Integer} n
# @return {Integer}
def tribonacci(n)
    trib(n, 0, 1, 1)
end

def trib(n, a, b, c)
    return a if n == 0
    return b if n == 1
    return c if n == 2
    trib(n - 1, b, c, a + b + c)
end