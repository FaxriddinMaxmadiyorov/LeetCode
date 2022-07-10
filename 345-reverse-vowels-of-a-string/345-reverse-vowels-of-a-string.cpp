class Solution {
public:
    bool inside(char c){
        if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' ||
           c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U')
            return true;
        return false;
    }
    
    string reverseVowels(string s) {
        int left = 0, right = s.size() - 1;
        bool l_found = false, r_found = false;
        while (left < right)
        {
            if (!l_found)
            {
                if (!inside(s[left])){
                    left++;
                }
                else
                    l_found = true;
            }
            
            if (!r_found)
            {
                if (!inside(s[right])){
                    right--;
                }
                else
                    r_found = true;
            }
            
            if (l_found && r_found){
                swap(s[left], s[right]);
                l_found = false;
                r_found = false;
                left++; right--;
            }
            // cout<<left<<" "<<right<<" "<<s<<endl;
        }
        return s;
    }
};