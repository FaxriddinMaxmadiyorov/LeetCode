class Solution {
public:
    vector<int> sortArrayByParity(vector<int>& nums) {
        int j = nums.size() - 1;
        for (int i = 0; i < nums.size(); i++)
        {
            if (nums[i] % 2 == 1){
                while (j >= i)
                {
                    if (nums[j] % 2 == 0){
                        swap(nums[i], nums[j]);
                        j--;
                        break;
                    }
                    j--;
                }
            }
        }
        return nums;
    }
};