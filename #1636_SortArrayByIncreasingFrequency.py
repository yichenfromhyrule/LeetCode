class Solution(object):
    def frequencySort(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        hashmap = {}
        for n in nums:
            if n in hashmap:
                hashmap[n] += 1
            else:
                hashmap[n] = 1
        a = sorted(hashmap.items(), key=lambda x: (x[1],(-1*x[0])))
        r = []
        for k in a:
            r += [k[0]] * k[1]
        return r