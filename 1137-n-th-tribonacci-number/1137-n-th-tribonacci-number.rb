# @param {Integer} n
# @return {Integer}
def tribonacci(n)
    f = Array.new
    f << 0
    f << 1
    f << 1
    for i in 3..n
        s = f[i-1]+f[i-2]+f[i-3]
        f << s
    end
    f[n]
end