class Solution {
public:
    bool isPerfectSquare(int num) {
        vector<int> squares;
        for (int i=1; i<=46340; i++)
            squares.push_back(i*i);
        for (auto i:squares){
            if (i==num)
                return true;
        }
        return false;
    }
};