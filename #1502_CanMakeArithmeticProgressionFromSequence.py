class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        arr.sort()
        r = [arr[i+1]-arr[i] for i in range(0, len(arr)-1)]
        return len(set(r)) == 1