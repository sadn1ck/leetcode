/*
 * Given an integer n, return 1 - n in lexicographical order.

For example, given 13, return: [1,10,11,12,13,2,3,4,5,6,7,8,9].

Please optimize your algorithm to use less time and space. The input size may be as large as 5,000,000.
 * */

class Solution {
public:
    vector<int> lexicalOrder(int n) {
        vector <string> store;
        for(int i =1;i<=n;i++){
            store.push_back(to_string(i));
        }
        sort(store.begin(), store.end());
        vector <int> fi;
        for(auto s: store){
            fi.push_back(stoi(s));
        }
        return fi;
    }
};
