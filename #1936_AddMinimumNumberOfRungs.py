class Solution(object):
    def addRungs(self, rungs, dist):
        """
        :type rungs: List[int]
        :type dist: int
        :rtype: int
        """
        rungs = [0] + rungs
        count = 0
        checking = rungs[0]
        for i in range(1, len(rungs)):
            if rungs[i] - checking > dist:
                r = (rungs[i] - checking) // dist
                r -= 1 if (rungs[i] - checking) % dist == 0 else 0
                count += r
                checking += (dist * r)
            checking = rungs[i]
        return count