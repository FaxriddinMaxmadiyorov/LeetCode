class Solution {
public:
    int two_power(int n){
        int p = 1;
        for (int i = 1; i <= n; i++)
            p *= 2;
        return p;
    }
    int findComplement(int num) {
        string s = "";
        while (num > 0){
            s += char(num % 2 + 48);
            num = num  / 2;
        }
        cout << s;
        for (int i = 0; i < s.size(); i++)
        {
            if (s[i] == '1')
                s[i] = '0';
            else
                s[i] = '1';
        }
        int sum = 0;
        for (int i = 0; i < s.size(); i++)
        {
            sum = sum + (s[i] - 48) * two_power(i);
        }
        return sum;
    }
};