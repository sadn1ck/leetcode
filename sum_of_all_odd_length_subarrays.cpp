/*
Given an array of positive integers arr, calculate the sum of all possible odd-length subarrays.

A subarray is a contiguous subsequence of the array.

Return the sum of all odd-length subarrays of arr.
 
*/
class Solution {
public:
    int sumOddLengthSubarrays(vector<int>& arr) {
        int sum = accumulate(arr.begin(), arr.end(), 0);
        vector<int> prefix;
        int itersum = 0;
        for(int i=0;i<arr.size();i++){
            itersum = itersum + arr.at(i);
            prefix.push_back(itersum);
        }
        itersum = 0;
        for(auto i: prefix){
            cout << i << " ";
        }
        cout <<"\n" << sum << "\n";
        for(int j=2;j<arr.size();j+=2){
            for(int i=0;i<=arr.size()-1-j;i++){
            if(i!=0){
                itersum = prefix[i+j] - prefix[i-1];
            } else {
                itersum = prefix[i+j];
            }
            cout << itersum << " " << sum << "\n";
            sum = sum + itersum;
        }
        }
        return sum;
    }
};
