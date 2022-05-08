class Solution {
public:
    int majorityElement(vector<int>& nums) {
        map<int,int>mp; int res, maxi=0;
        for (int i=0; i<nums.size(); i++)
                mp[nums[i]]++;
        for (auto it:mp)
        {
            if (it.second>maxi){
                res=it.first;
                maxi=it.second;
            }
        }
        return res;
    }
};