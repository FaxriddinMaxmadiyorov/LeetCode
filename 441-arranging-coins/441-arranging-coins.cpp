class Solution {
public:
    int arrangeCoins(int n) {
        int t = 1, k = 0;
        while (n > 0)
        {
            if (n - t >= 0)
                n -= t, k++, t++;
            else
                break;
        }
        return k;
    }
};