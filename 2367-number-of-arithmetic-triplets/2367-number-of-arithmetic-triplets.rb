class Solution {
public:
    int arithmeticTriplets(vector<int>& nums, int diff) {
        int c = 0;
        for (int i = 0; i < nums.size(); i++)
        {
            for (int j= i + 1; j < nums.size(); j++)
            {
                int diff1 = nums[j] - nums[i];
                for (int k = j + 1; k < nums.size(); k++)
                {
                    int diff2 = nums[k] - nums[j];
                    if (diff1 == diff2 && diff1 == diff)
                        c++;
                }
            }
        }
        return c;
    }
};