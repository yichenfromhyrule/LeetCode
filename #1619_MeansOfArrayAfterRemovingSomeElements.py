class Solution(object):
    def trimMean(self, arr):
        """
        :type arr: List[int]
        :rtype: float
        """
        arr.sort()
        l = len(arr)
        return (sum(arr[l//20: -l//20])) / (l*0.9)