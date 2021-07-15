class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        coins.sort()
        dp = [[-1 for i in range(len(coins))] for j in range(amount+1)]
        for m in range(0, amount+1):
            for n in range(0, len(coins)):
                if m == 0:
                    dp[m][n] = 0
                elif m == coins[n]:
                    dp[m][n] = 1
                elif m > coins[n] and n == 0:
                    dp[m][n] = dp[m - coins[n]][n] + 1 if dp[m - coins[n]][n] != -1 else -1
                elif m < coins[n]:
                    dp[m][n] = dp[m][n-1]
                else:
                    if dp[m][n-1] == -1 and dp[m-coins[n]][n] == -1:
                        dp[m][n] = -1
                    elif dp[m][n-1] == -1:
                        dp[m][n] = dp[m-coins[n]][n] + 1
                    elif dp[m-coins[n]][n] == -1:
                        dp[m][n] = dp[m][n-1]
                    else:
                        dp[m][n] = min(dp[m-coins[n]][n]+1, dp[m][n-1])
        return dp[amount][len(coins)-1]

if __name__ == '__main__':
    s = Solution()
    coins1 = [186,419,83,408]
    amount1 = 6249
    coins = [3, 6, 7]
    amount = 10
    r = s.coinChange(coins1, amount1)
    print(r)
