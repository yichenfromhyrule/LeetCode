class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        if len(arr) < 3:
            return False
        else:
            top = max(arr)
            top_index = arr.index(top)
            if top_index == 0 or top_index == (len(arr)-1):
                return False
            else:
                for i in range(1, top_index):
                    if arr[i] <= arr[i-1]:
                        return False
                for j in range(top_index, len(arr) - 1):
                    if arr[j] <= arr[j+1]:
                        return False
                return True