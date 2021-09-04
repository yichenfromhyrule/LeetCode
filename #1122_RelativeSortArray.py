class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        hashmap = {}
        for num1 in arr1:
            if num1 not in hashmap:
                hashmap[num1] = 1
            else:
                hashmap[num1] += 1
        result = []
        for num2 in arr2:
            result += [num2] * hashmap[num2]
            del hashmap[num2]
        last = list(hashmap.keys())
        last.sort()
        for l in last:
            result += [l] * hashmap[l]
        return result