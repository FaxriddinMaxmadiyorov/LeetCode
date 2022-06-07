class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int start = 0;
        for (int i=0; i<nums.size(); i++)
        {
            if (nums[i] == 0)
            {
                int start = i;
                while (nums[start] == 0)
                {
                    start++;
                    if (start >= nums.size())
                        return;
                }
                swap(nums[i], nums[start]);
            }
        }
    }
};