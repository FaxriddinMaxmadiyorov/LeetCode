class Solution {
public:
    void show(map<int, int> mp)
    {
        for (auto i : mp)
            cout<<i.first<<" "<<i.second<<endl;
    }
    bool isIsomorphic(string s, string t) {
        map<int, int> mp;
        for (int i = 0; i < s.size(); i++)
        {
            // show(mp);
            if (mp.count(int(s[i])) > 0 && mp[int(s[i])] != int(t[i]))
                return false;
            for (auto it : mp)
            {
                if (int(t[i]) == it.second && s[i] != it.first)
                    return false;
            }
            mp[int(s[i])] = int(t[i]);
        }
        return true;
    }
};