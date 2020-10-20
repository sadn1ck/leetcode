class Solution {
public:
    int majorityElement(vector<int>& nums) {
        map<int, int> mp;
        int n = nums.size();
        for(auto x: nums){
            mp[x]++;
        }
        for(auto it: mp){
            // cout << it.first << " "<< it.second<<endl;
            if(it.second > n/2){
                return it.first;
            }
        }
        return -1;
    }
};