class Solution(object):
    def checkStraightLine(self, c):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """
        c.sort()
        c1 = [s[0] for s in c]
        c2 = [s[1] for s in c]
        if len(set(c1)) == 1 or len(set(c2)) == 1:
            return True
        else:
            if (c[1][0] - c[0][0]) == 0:
                return False
            else:
                p = (c[1][1] - c[0][1]) / (c[1][0] - c[0][0])
                for i in range(1, len(c)-1):
                    if (c[i+1][0] - c[i][0]) == 0:
                        return False
                    else:
                        if (c[i+1][1] - c[i][1]) / (c[i+1][0] - c[i][0]) != p:
                            return False
                return True