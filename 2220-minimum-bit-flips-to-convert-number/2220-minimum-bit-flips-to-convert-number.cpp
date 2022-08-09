class Solution {
public:
    string DecimalToBinary(int n){
        string res = "";
        while (n > 0){
            res += char(n % 2 + 48);
            n = n / 2;
        }
        res += char(n % 2 + 48);
        reverse(res.begin(), res.end());
        return res;
    }
    
    int minBitFlips(int start, int goal) {
        int temp = start ^ goal, c = 0;
        string BinaryXor = DecimalToBinary(temp);
        for (int i = 0; i < BinaryXor.size(); i++)
        {
            if (BinaryXor[i] == '1')
                c++;
        }
        return c;
    }
};