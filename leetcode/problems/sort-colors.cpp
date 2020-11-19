/*
 *
 * Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

 Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

 Follow up:

     Could you solve this problem without using the library's sort function?
     Could you come up with a one-pass algorithm using only O(1) constant space?

 * */
class Solution {
    public:
        void sortColors(vector<int>& nums) {
            int z = 0, o = 0, t = 0;
            for(auto n: nums){
                if(n==0) z++;
                if(n==1) o++;
                if(n==2) t++;

            }
            cout << z << " " <<o << " "<< t << "\n";
            for(int i = 0;i<z;i++){
                nums[i] = 0;

            }
            for(int i = 0 + z;i<z + o;i++){
                nums[i] = 1;

            }
            for(int i = o + z;i<o + z + t;i++){
                nums[i] = 2;

            }

        }

};
