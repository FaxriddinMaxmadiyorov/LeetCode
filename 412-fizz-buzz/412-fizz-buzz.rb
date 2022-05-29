# @param {Integer} n
# @return {String[]}
def fizz_buzz(n)
    ans = Array.new()
    for i in 1..n
        if i % 15 == 0
            ans<<("FizzBuzz")
        elsif i % 3 == 0
            ans<<("Fizz")
        elsif i % 5 == 0
            ans<<("Buzz")
        else
            ans<<(i.to_s)
        end
    end
    return ans
end