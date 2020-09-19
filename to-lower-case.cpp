/*
Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.
*/
class Solution {
public:
    string toLowerCase(string str) {
        string res = "";
        for(auto c: str){
            if (c >= 65 && c <= 90){
                res = res + (char)(c+32);
            } else {
                res = res + c;
            }
        }
        return res;
    }
};
