/*
Given a valid (IPv4) IP address, return a defanged version of that IP address.

A defanged IP address replaces every period "." with "[.]".
*/
class Solution {
public:
    string defangIPaddr(string address) {
        
        string ip="";
        
        for(int i=0;i<address.length();i++){
            cout << address[i] << " ";
            if (address[i] == '.'){
                ip += "[.]";
            }
            else {
                ip += address[i];
            }
        }
        return ip;
    }
};
