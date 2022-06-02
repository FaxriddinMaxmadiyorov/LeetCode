def next_greatest_letter(letters, target)
    low, up = 0, letters.length - 1
    while low <= up
       middle = (low + up) / 2
       if letters[middle] > target
           up = middle - 1
       elsif letters[middle] <= target
           low = middle + 1
       end
    end
    puts low, up
    return letters[low % letters.length]
end