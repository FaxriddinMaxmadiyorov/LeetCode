# @param {Integer} num
# @return {String}
def convert_to_base7(num)
    return '-' + convert_to_base7(-num) if num < 0 
    return num.to_s if num < 7
    return convert_to_base7(num / 7) + (num % 7).to_s
end