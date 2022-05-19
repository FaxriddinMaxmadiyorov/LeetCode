class Solution {
public:
    string reverseOnlyLetters(string s) {
        int i = 0, j = s.size()-1;
        bool fi = false, fj = false;
        while (i < j)
        {
            if (!fi && ((s[i] >= 'a' && s[i] <= 'z') || (s[i] >= 'A' && s[i] <='Z')))
                fi = true;
            if (!fj && ((s[j] >= 'a' && s[j] <= 'z') || (s[j] >= 'A' && s[j] <='Z')))
                fj = true;
            if (fi && fj)
            {
                swap(s[i], s[j]);
                fi = false, fj = false;
            }
            if (!fi)
                i++;
            if (!fj)
                j--;
        }
        return s;    
    }
};