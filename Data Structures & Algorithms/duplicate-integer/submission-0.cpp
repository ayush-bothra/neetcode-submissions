class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_map<int,int> store;
        for(int num : nums)
        {
            store[num]++;
            if(store[num] > 1) return true;
        }
        return false;
    }
};
