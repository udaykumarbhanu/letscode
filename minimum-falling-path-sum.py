"""LC: 931. Minimum Falling Path Sum
Given a square array of integers A, we want the minimum sum of a falling path
through A.

A falling path starts at any element in the first row, and chooses one element
from each row.  The next row's choice must be in a column that is different from
the previous row's column by at most one.

Example 1:
Input: [[1,2,3],[4,5,6],[7,8,9]]
Output: 12
Explanation:
The possible falling paths are:
[1,4,7], [1,4,8], [1,5,7], [1,5,8], [1,5,9]
[2,4,7], [2,4,8], [2,5,7], [2,5,8], [2,5,9], [2,6,8], [2,6,9]
[3,5,7], [3,5,8], [3,5,9], [3,6,8], [3,6,9]
The falling path with the smallest sum is [1,4,7], so the answer is 12.

Note:
1 <= A.length == A[0].length <= 100
-100 <= A[i][j] <= 100
"""

class Solution(object):
    def minFallingPathSum(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        if not A:
            return 0

        r = len(A)
        c = len(A[0])
        # print r, c

        dp = [[0]*(c) for i in range(r)]
        # print len(dp), len(dp[0])

        # fill first row with first row of matrix A.
        for j in range(c):
            dp[0][j] = A[0][j]

        for i in range(1, r):
            for j in range(c):
                # print i, j
                #first column.
                if j == 0:
                    dp[i][j] = A[i][j] + min(dp[i-1][j], dp[i-1][j+1])
                #last column.
                elif j == c-1:
                    dp[i][j] = A[i][j] + min(dp[i-1][j], dp[i-1][j-1])
                else:
                    dp[i][j] = A[i][j] + min(dp[i-1][j-1], dp[i-1][j], dp[i-1][j+1])

        return min(dp[-1])

if __name__ == '__main__':
    A = [[1,2,3],[4,5,6],[7,8,9]]
    print Solution().minFallingPathSum(A)
