class Solution(object):
    def containsPattern(self, arr, m, k):
        """
        :type arr: List[int]
        :type m: int
        :type k: int
        :rtype: bool
        """
        for i in range(0, len(arr)):
            if i + (m * k) - 1 >= len(arr):
                return False
            else:
                l = arr[i:i + m] * k
                if l == arr[i: i + (m * k)]:
                    return True
        return False
