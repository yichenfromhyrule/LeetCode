class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dp = [False for index in range(len(s))]
        for i in range(0, len(s)):
            for word in wordDict:
                if word == s[i + 1 - len(word):i + 1] and (dp[i - len(word)] or (i + 1 - len(word)) == 0):
                    dp[i] = True
        return dp[-1]


if __name__ == '__main__':
    s = Solution()
    str = "catsandog"
    wordDict = ["cats","dog","sand","and","cat"]
    r = s.wordBreak(str, wordDict)
    print(r)