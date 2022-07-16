class Solution {
public:
    string decodeMessage(string key, string message) {
        map<char, char> mp; int index = 97;
        for (int i=0; i<key.size(); i++){
            if (mp.count(key[i]))
                continue;
            else if (key[i]!= ' ')
                mp[key[i]] = char(index), index++;
        }
        for (auto it:mp){
            cout<<it.first<<" "<<it.second<<endl;
        }
        string res = "";
        for (int i = 0; i<message.size(); i++){
            char t = message[i];
            if (t != ' ')
                res += mp[t];
            else
                res += t;
        }
        return res;
    }
};