class Solution(object):
    def canFormArray(self, arr, pieces):
        """
        :type arr: List[int]
        :type pieces: List[List[int]]
        :rtype: bool
        """
        hashmap = {}
        for i in range(len(arr)):
            hashmap[arr[i]] = i
        for p in pieces:
            if len(p) > 1:
                if p[0] not in arr:
                    return False
                else:
                    start_index = hashmap[p[0]]
                    for j in range(1, len(p)):
                        if p[j] not in arr:
                            return False
                        else:
                            if hashmap[p[j]] == start_index + 1:
                                start_index += 1
                            else:
                                return False
            else:
                if p[0] not in arr:
                    return False
        return True
