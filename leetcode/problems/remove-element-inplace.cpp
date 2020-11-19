/*
Given an array nums and a value val, remove all instances of that value in-place and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.
*/

aclass Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int count = nums.size();
        vector<int>::iterator it = nums.begin(); 
        while(it!=nums.end()){
            if (*it == val){
                cout <<*it << " "; 
                nums.erase(it--);
                count--;
            }
            it++;
        }
        return count;
    }
};
