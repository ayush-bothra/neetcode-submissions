class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char,int> store;
        for(char c : s)
        {
            store[c]++;
        } 
        for(char c : t)
        {
            store[c]--;
        }

        for(int  i =0; i< store.size(); i++)
        {
            if(store[i] != 0) return false;
        }
        return true;
    }
};
