class Solution {
public:
    int singleNonDuplicate(vector<int>& nums) {
        int ans=nums.at(0);
        for(int i=1;i<nums.size();i++){
            ans = ans ^ nums.at(i);
        }
        return ans;
    }
};
// Binary Search solution is logn, but the xor solution is more intuitive
// **********************************************************************
// class Solution {
// public:
//     int singleNonDuplicate(vector<int>& nums) {
//         if (nums.size()==1) {
//             return nums[0];
//         } 
//         if (nums[0]!=nums[1]) {
//             return nums[0];
//         }
//         int n=nums.size();
//         if (nums[n-1] != nums[n-2]) {
//             return nums[n-1];
//         }
//         int left=0;
//         int right=nums.size()-1;
//         while (left<=right) {
//             int mid=left+(right-left)/2;
//             if (nums[mid]!=nums[mid+1] && nums[mid] != nums[mid-1]) {
//                 return nums[mid];
//             }
//             //element has only one single non duplicate
//             //even-odd size zone
//             if (mid%2==0 and nums[mid]==nums[mid+1]) {
//                 //mid%2==0, means even index, so left size has even number of elements
//                 left=mid+1;
//             } else if (mid%2==1 and nums[mid]==nums[mid-1]) {
//                 //mid%2==1 means odd index, so left size has even number of elements
//                 //including mid
//                 left=mid+1;
//             } else {
//                 right=mid-1;
//             }
//         }
//         return -1;
//     }
// };