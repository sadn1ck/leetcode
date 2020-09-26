/*
Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.
*/

class Solution {
public:
    vector<int> sortedSquares(vector<int>& A) {
        vector<int> res(A.size());
        
        int l = 0, r = A.size() - 1;
        
        for (int k = A.size() - 1; k >= 0; k--) {
            if (abs(A[l]) > abs(A[r])){
                res[k] = A[l]*A[l];
                l++;
            } else {
                res[k] = A[r]*A[r];
                r--;
            }
        }
        return res;
    }
};
