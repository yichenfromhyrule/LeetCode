class Solution(object):
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        arr1 = [(arr[i]-(i+1)) for i in range(len(arr))]
        if k > arr1[-1]:
            return arr[-1]+k-arr1[-1]
        else:
            for j in range(len(arr1)):
                if arr1[j] >= k:
                    if j > 0:
                        return arr[j-1]+k-arr1[j-1]
                    else:
                        return k