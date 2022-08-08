class Solution {
public:
    bool IsSquare(int n)
    {
        int m = sqrt(n);
        return m * m == n;
    }
    int countTriples(int n) {
        int c = 0;
        for (int i = 1; i < n; i++)
        {
            for (int j = i + 1; j < n; j++)
            {
                if (IsSquare(i * i + j * j) && i * i + j * j <= n * n)
                    // cout<<i<<" "<<j<<"  "<<i * i + j * j<<endl;
                    c++;
            }
        }
        return 2 * c;
    }
};