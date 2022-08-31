class Solution {
public:
    bool isUp(char c){
        if (c >= 65 && c <= 90)
            return true;
        return false;
    }
    
    bool isLow(char c){
        if (c >= 97 && c <= 122)
            return true;
        return false;
    } 
    
    bool detectCapitalUse(string word) {
        int n = word.size(); bool all_cap = false, only_first_cap = false;
        // all letters are capital
        if (isUp(word[0])){
            if (isUp(word[1]))
                all_cap = true;
            else
                only_first_cap = true;
            for (int i = 2; i < n; i++)
            {
                if (all_cap && isLow(word[i]))
                    return false;
                if (only_first_cap && isUp(word[i]))
                    return false;
            }
        }
        // all letters are not capital
        if (isLow(word[0])){
            for (int i = 1; i < n; i++)
            {
                if (isUp(word[i]))
                    return false;
            }
        }
        return true;
    }
};