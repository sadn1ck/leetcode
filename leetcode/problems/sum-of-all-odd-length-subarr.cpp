/*
Given an array of positive integers arr, calculate the sum of all possible odd-length subarrays.

A subarray is a contiguous subsequence of the array.

Return the sum of all odd-length subarrays of arr.

*/

class Solution {
public:
    /*
        consider this array [1, 2, 3, 4, 5].
        the idea is choose one index and calculate its contribution to the ans.
        To do that we must figure out how many times a given element occurs in an odd array.
        lets choose 2 for example, 2 occurs in [2], [1, 2, 3], [2, 3, 4], [1, 2, 3, 4, 5] ie 4 times.
        to find that i am seperating the array about element 2 hence the two arrays become [1, 2] and [2, 3, 4, 5].
        now its just combinations, we need to choose a start point from first part and end point from second.
        we can do that in sizeOfFirstPart*sizeOfSecondPart ways i.e. 2*4 ways. now half of these will be of odd length.
        so the to calculate the contribution of 2 we just multily it with no. of times it occurs in an odd array. 
    */
    int sumOddLengthSubarrays(vector<int>& arr) {
        int sum = 0;
        for(int i=0; i<arr.size(); i++){
            sum+= arr[i]*(ceil((arr.size()-i)*(i+1)/2.0));
        }
        return sum;
    } 
    
    int sumOddLengthSubarrays2(vector<int>& arr) {
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
