# @param {Integer[]} candy_type
# @return {Integer}
def distribute_candies(candy_type)
    candies = Set.new()
    for candy in candy_type
        candies << candy
    end
    return [candies.length, candy_type.length / 2].min
end