/*
Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].

Return the answer in an array.
*/

class Solution {
public:
    vector<int> smallerNumbersThanCurrent(vector<int>& nums) {
        int count = 0;
        vector<int> smol;
        for (int i = 0; i< nums.size();i++){
            for (int j = 0; j< nums.size();j++){
                if (i != j){
                    if (nums[i] > nums[j]){
                        count++;
                    }
                }
            }
            smol.push_back(count);
            count = 0;
        }
        return smol;
    }
};
