class Solution {
public:
    int arrangeCoins(long long n) {
        long long left = 1, right = 123456789;
        while (left <= right)
        {
            long long middle = (left + right) / 2;
            long long sum = middle * (middle + 1) / 2;
            if (sum > n)
                right = middle - 1;
            else if (sum < n)
                left = middle + 1;
            else 
                return middle;
        }
        return right;
    }
};