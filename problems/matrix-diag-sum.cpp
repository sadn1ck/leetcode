/*
Given a square matrix mat, return the sum of the matrix diagonals.

Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal that are not part of the primary diagonal.
*/
class Solution {
public:
    int diagonalSum(vector<vector<int>>& mat) {
        int sum = 0;
        int N = mat.size();
        for (int i=0; i < N; ++i)
            sum += mat[i][i] + mat[i][N - 1 - i];
        if (N % 2 != 0)
            sum = sum - mat[N/2][N/2];
        return sum;
    }
};

