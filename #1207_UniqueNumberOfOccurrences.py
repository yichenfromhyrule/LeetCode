class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        hashmap = {}
        for a in arr:
            if a in hashmap:
                hashmap[a] += 1
            else:
                hashmap[a] = 1
        l = list(hashmap.values())
        return len(l) == len(set(l))
