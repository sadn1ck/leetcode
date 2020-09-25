/*
You are given an integer array nums sorted in ascending order, and an integer target.

Suppose that nums is rotated at some pivot unknown to you beforehand (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

If target is found in the array return its index, otherwise, return -1.
*/
class Solution {
public:
    int search(vector<int>& nums, int target) {
        auto iter = find(nums.begin(), nums.end(), target);
        if( iter != nums.end()){
            return(distance(nums.begin(), iter));
        } else { 
            return -1;
        }
    }
};
