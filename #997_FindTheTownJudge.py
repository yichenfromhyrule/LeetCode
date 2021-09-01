class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        if n == 1 and trust == []:
            return 1
        else:
            people1 = [0] * n
            people2 = [0] * n
            for t in trust:
                people1[t[1] - 1] += 1
                people2[t[0] - 1] = 1
            for i in range(n):
                if people2[i] == 0 and people1[i] == n - 1:
                    return i + 1
            return -1
