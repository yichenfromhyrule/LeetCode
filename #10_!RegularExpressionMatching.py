import numpy as np
#class Solution(object):
def isMatch(s, p):

        dp = np.full((len(s), len(p)), False)

        counter=0
        # 1. Set first row
        for i in range(0, len(p)):
            if s[0]==p[i]:
                if counter == 0:
                    dp[0][i]=True
                    counter+=1
                else:
                    dp[0][i]=False
            elif p[i]==".":
                if counter == 0:
                    dp[0][i]=True
                    counter+=1
                else:
                    if i>0 and p[i-1]=="*":
                        dp[0][i]=True
                    else:
                        dp[0][i]=False
            elif p[i]=="*":
                if i>0:
                    if i==1:
                        dp[0][i] = dp[0][i - 1]
                    else:
                        dp[0][i]=dp[0][i-2] or dp[0][i-1]
            else:
                dp[0][i]=False

        # 2. Set first column
        if len(s)>0:
            for i in range(1, len(s)):
                if p[0]=="*":
                    dp[i][0]=dp[i-1][0]
                else:
                    dp[i][0]=False

        # 3. Set others
        if len(s)>0 and len(p)>0:
            for i in range(1, len(s)):
                for j in range(1, len(p)):
                    if p[j]==s[i]:
                        dp[i][j] = dp[i-1][j-1]
                    elif p[j]==".":
                        if p[j-1]=="*":
                            dp[i][j] = dp[i-1][j-2]
                        else:
                            dp[i][j] = dp[i - 1][j - 1]
                    elif p[j]=="*":
                        if p[j-1]==s[i] or p[j-1]==".":
                            dp[i][j] = dp[i - 1][j - 1] or dp[i][j-1]
                        else:
                            dp[i][j]=dp[i][j-2]
                    else:
                        dp[i][j]=False


        print(dp)
        return dp[len(s)-1][len(p)-1]


isMatch("mississippi","mis*is*ip*.")