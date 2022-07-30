"""
  @source: https://leetcode.com/problems/longest-palindromic-substring/
  @param {string} s
  @return {string}
"""
from functools import lru_cache


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        @lru_cache(None)
        def dp(i, j):
            if obstacleGrid[i][j] == 1 or obstacleGrid[0][0] == 1:
                return 0
            elif i == 0 and j == 0:
                return 1
            elif i == 0:
                return dp(i,j-1)
            elif j == 0:
                return dp(i-1,j)
            else:
                return dp(i-1,j) + dp(i,j-1)

        return dp(m - 1, n - 1)
        


