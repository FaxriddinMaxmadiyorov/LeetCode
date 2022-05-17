class Solution {
public:
    bool yesno(string &s){
        int i = 0, j = s.size()-1;
        while (i < j)
        {
            if (s[i] == s[j])
                i++, j--;
            else
                return false;
        }
        return true;
    }
    string firstPalindrome(vector<string>& words) {
        for (auto str: words){
            if (yesno(str))
                return str;
        }
        return "";
    }
};