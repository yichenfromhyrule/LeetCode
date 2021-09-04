class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        result = []
        n = len(arr)
        i = 0
        while len(result) < n:
            if arr[i] == 0:
                result.append(0)
                result.append(0)
            else:
                result.append(arr[i])
            i+=1
        for i in range(n):
            arr[i] = result[i]