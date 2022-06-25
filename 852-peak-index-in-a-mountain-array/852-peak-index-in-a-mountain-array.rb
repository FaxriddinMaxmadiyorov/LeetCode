def peak_index_in_mountain_array(arr)
    low, high = 0, arr.length  
    return f(low, high, arr)
end

def f(low, high, arr)
    if low == high
        return low    
    end
    
    mid = (low + high) / 2
    if mid > 0 and mid < arr.length and arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]
        return mid
    elsif arr[mid] < arr[mid + 1]
        low = mid + 1
    else
        high = mid - 1
    end
    
    return f(low, high, arr)
end