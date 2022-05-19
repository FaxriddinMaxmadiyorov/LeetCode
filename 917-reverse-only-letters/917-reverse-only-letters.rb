# @param {String} s
# @return {String}
def reverse_only_letters(s)
    i, j = 0, s.length - 1
    fi, fj = false, false
    while i < j
       if !fi && ((s[i] >= 'a' && s[i] <= 'z') || (s[i] >= 'A' && s[i] <='Z'))
           fi = true
       end
        
        if !fj && ((s[j] >= 'a' && s[j] <= 'z') || (s[j] >= 'A' && s[j] <='Z'))
           fj = true 
        end
        
        if fi && fj
            s[i], s[j] = s[j], s[i]
            fi = false
            fj = false
        end
        if fi == false
            i += 1
        end
        if fj == false
            j -= 1
        end
    end
    return s
end