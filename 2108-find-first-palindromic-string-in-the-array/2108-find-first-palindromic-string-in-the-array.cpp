class Solution {
public:
    bool yesno(string s){
        string temp=s;
        reverse(s.begin(), s.end());
        return s == temp;
    }
    string firstPalindrome(vector<string>& words) {
        for (auto str: words){
            if (yesno(str))
                return str;
        }
        return "";
    }
};