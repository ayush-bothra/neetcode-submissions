class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int,int> store;
        vector<int> result;
        for(int i=0; i<nums.size(); i++)
        {
            unordered_map<int,int>:: iterator it = store.begin();
            if(store.find(target-nums[i]) != store.end())
            {
                it = store.find(target-nums[i]);
                result.push_back(it->second);
                result.push_back(i);
                break;
            }
            else
            {
                store[nums[i]] = i;
            }
        }
        return result;
    }
};
