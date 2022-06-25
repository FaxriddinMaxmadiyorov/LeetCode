def peak_index_in_mountain_array(a)
    return find_mountain_index_from(0, a.length - 1, a)
end

def find_mountain_index_from(start_idx, end_idx, a)
    if start_idx == end_idx
        return start_idx
    end

    midpoint = (end_idx + start_idx) / 2
    if (a[midpoint] > a[midpoint - 1] && a[midpoint] > a[midpoint + 1]) 
        return midpoint
    elsif a[midpoint] < a[midpoint + 1] # too small; move right
        return find_mountain_index_from(midpoint + 1, end_idx, a)
    else # too big; move left
        return find_mountain_index_from(start_idx, midpoint, a)
    end
end