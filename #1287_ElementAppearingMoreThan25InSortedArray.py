class Solution(object):
    def findSpecialInteger(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        if len(set(arr)) == 1:
            return arr[0]
        else:
            o = len(arr) / 4
            check = arr[0]
            count = 0
            for i in range(0, len(arr)):
                if arr[i] == check:
                    count += 1
                else:
                    if count > o:
                        return arr[i - 1]
                    else:
                        check = arr[i]
                        count = 1
            if count > o:
                return arr[-1]
