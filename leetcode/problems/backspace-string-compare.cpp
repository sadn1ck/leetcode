/*
Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

Note that after backspacing an empty text, the text will continue empty.
*/
class Solution {
public:
    bool backspaceCompare(string S, string T) {
        vector<char> vecs, vect;
        for(auto x: S){
            if(vecs.size()>0){
                if(x=='#'){
                    vecs.pop_back();
                }
            }
            if(x!='#'){
                vecs.push_back(x);
            }
        }
        for(auto x: T){
            if(vect.size()>0){
                if(x=='#'){
                    vect.pop_back();
                }
            }
            if(x!='#'){
                vect.push_back(x);
            }
        }
        if(vecs.size()!=vect.size()){
            return false;
        }
        else{
            for(int i=0;i<vect.size();i++){
                if(vect[i]!=vecs[i]){
                    return false;
                }
            }
        }
        return true;
    }
};
