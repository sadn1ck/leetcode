// The API isBadVersion is defined for you.
// bool isBadVersion(int version);

class Solution {
public:
    int firstBadVersion(int n) {
        unsigned long long l=1;
        unsigned long long r=n;
        unsigned long long mid = (l+r)/2;
        while(l<r){
            if(isBadVersion(mid)){
                r = mid;
            }
            else {
                l = mid+1;
            }
            mid = (l+r)/2;
        }
        return mid;
    }
};
// First Bad Version
