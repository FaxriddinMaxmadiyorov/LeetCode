class Solution {
public:
    vector<int> countBits(int n) {
        vector<int> a;
        // 0 -> 0          0 
        // 1 -> 1          1
        // 2 -> 1          1
        // 3 -> 11         2
        // 4 -> 100        1
        // 5 -> 101        2
        // 6 -> 110        2
        // 7 -> 111        3
        // 8 -> 1000       1
        // 9 -> 1001       2
        // 10 -> 1010      2
        // 11 -> 1011      3
        // 12 -> 1100      2
        // 13 -> 1101      3
        // 14 -> 1110      3
        // 15 -> 1111      4
        // 16 -> 10000     1
        a.push_back(0);
        for (int i = 1; i <= n; i++)
        {
            if (i % 2 == 1)
                a.push_back(a[i - 1] + 1);
            else
                a.push_back(a[i / 2]);
        }
        return a;
    }
};