class Solution {
public:
    string reverseWords(string s) {
        string ans = "", temp = "";
        for (int i = 0; i < s.size(); i++)
        {
            if (s[i] != ' ')
            {
                temp += s[i];
            }
            else{
                reverse(temp.begin(), temp.end());
                ans = ans + temp + ' ';
                temp.clear();
            }
        }
        reverse(temp.begin(), temp.end());
        ans += temp;
        return ans;
    }
};