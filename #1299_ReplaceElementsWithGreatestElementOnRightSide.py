class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        max_num = max(arr)
        arr += [-1]
        for i in range(0, len(arr) - 1):
            if arr[i] == max_num:
                max_num = max(arr[i + 1:])
            arr[i] = max_num
        return arr[:-1]
