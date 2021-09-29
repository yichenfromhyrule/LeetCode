class Solution(object):
    def minOperations(self, logs):
        """
        :type logs: List[str]
        :rtype: int
        """
        r = 0
        for log in logs:
            if log == "../":
                r = r - 1 if r > 0 else r
            elif log == "./":
                r = r
            else:
                r += 1
        return r
