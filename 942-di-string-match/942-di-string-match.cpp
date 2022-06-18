class Solution {
public:
    vector<int> diStringMatch(string s) {
        vector<int> res;
        int low = 0, high = s.size(), i = 0;
        while (low <= high)
        {
            if (s[i] == 'I')
            {
                res.push_back(low);
                low++;
            }
            else{
                res.push_back(high);
                high--;
            }
            i++;
        }
        return res;
    }
};