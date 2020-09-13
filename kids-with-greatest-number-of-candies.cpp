/*
Given the array candies and the integer extraCandies, where candies[i] represents the number of candies that the ith kid has.

For each kid check if there is a way to distribute extraCandies among the kids such that he or she can have the greatest number of candies among them. Notice that multiple kids can have the greatest number of candies.
*/


class Solution {
public:
    vector<bool> kidsWithCandies(vector<int>& candies, int extraCandies) {
        vector<bool> possible;
        long long most = *max_element(candies.begin(), candies.end());
        for(auto x: candies){
            possible.push_back(x+extraCandies >= most);
        }
        return possible;
    }
};