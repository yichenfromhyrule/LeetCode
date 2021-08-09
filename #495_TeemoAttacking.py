class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        result = 0
        for i in range(0, len(timeSeries)):
            if i + 1 < len(timeSeries):
                if timeSeries[i] + duration <= timeSeries[i + 1]:
                    result += duration
                else:
                    result += timeSeries[i + 1] - timeSeries[i]
            else:
                result += duration
        return result
