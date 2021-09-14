class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        list_set = set(arr)
        result = [-1]
        for num in list_set:
            if num == arr.count(num):
                result.append(num)
        return max(result)