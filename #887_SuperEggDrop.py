import numpy as np
def superEggDrop(k, n):
    """
    :type k: int
    :type n: int
    :rtype: int
    """
    dp = np.full((n,k),0)
    for i in range(0,k):
        dp[0][i]=1
    for i in range(0,n):
        if i>0:
            dp[i][0]=dp[i-1][0]+1
    if n>1 and k>1:
        for i in range (1,n):
            for j in range(1, k):
                dp[i][j] = dp[i-1][j-1]+dp[i-1][j]+1
    #print(dp)
    for i in range(0,n):
        if dp[i][k-1]>=n:
            #print(i+1)
            return (1+i)



superEggDrop(1,3)