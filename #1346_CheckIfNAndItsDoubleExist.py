from collections import Counter


class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        c = Counter(arr)
        if c[0] >= 2:
            return True
        else:
            for num in c.keys():
                if num * 2 in c and num != 0:
                    return True
            return False
