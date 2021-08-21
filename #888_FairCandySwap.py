class Solution(object):
    def fairCandySwap(self, aliceSizes, bobSizes):
        """
        :type aliceSizes: List[int]
        :type bobSizes: List[int]
        :rtype: List[int]
        """
        t = (sum(aliceSizes) - sum(bobSizes)) // 2
        bobSet = set(bobSizes)
        aliceSet = set(aliceSizes)
        for bob in bobSet:
            if (bob + t) in aliceSet:
                return(bob + t, bob)