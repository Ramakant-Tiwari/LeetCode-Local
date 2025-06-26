#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [-1 for _ in range(n+1)]
        # def solve(currStairCase, lastStairCase):
        #     if currStairCase > lastStairCase: return 0
        #     if currStairCase == lastStairCase: return 1

        #     if memo[currStairCase] == -1:
        #         memo[currStairCase] = solve(currStairCase+1, lastStairCase) + solve(currStairCase+2, lastStairCase)

        #     return memo[currStairCase]
        
        memo[0] = 1
        memo[1] = 1

        for currStairCase in range(2, n+1): 
            memo[currStairCase] = memo[currStairCase-2] + memo[currStairCase-1]
        
        print(memo)
        return memo[n]

        
        # return solve(0, n)
            
        
# @lc code=end

