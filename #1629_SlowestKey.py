class Solution(object):
    def slowestKey(self, r, k):
        """
        :type releaseTimes: List[int]
        :type keysPressed: str
        :rtype: str
        """
        r = [0] + r
        d = [(r[i+1]-r[i]) for i in range (len(r)-1)]
        max_d = max(d)
        c = []
        for i in range(len(d)):
            if d[i] == max_d:
                c.append(k[i])
        c.sort()
        return c[-1]