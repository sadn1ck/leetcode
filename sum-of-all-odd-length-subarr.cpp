class Solution {
public:
    int sumOddLengthSubarrays(vector<int>& arr) {
        int sum = 0;
        for(int i=0; i<arr.size(); i++){
            sum+= arr[i]*(ceil((arr.size()-i)*(i+1)/2.0));
        }
        return sum;
    }
};
