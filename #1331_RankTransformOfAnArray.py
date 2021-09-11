class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        if len(arr) == 0:
            return []
        else:
            arr_sort = sorted(arr)
            hashmap = {}
            checking = arr_sort[0]
            checking_index = 1
            hashmap[checking] = checking_index
            for i in range(0, len(arr_sort)):
                if arr_sort[i] != checking:
                    checking = arr_sort[i]
                    checking_index +=1
                    hashmap[checking] = checking_index
            result = []
            for num in arr:
                result.append(hashmap[num])
            return result