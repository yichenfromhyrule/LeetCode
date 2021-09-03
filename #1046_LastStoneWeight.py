class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        while len(stones) > 1:
            stones.sort(reverse=True)
            stone1 = stones.pop(0)
            stone2 = stones.pop(0)
            if stone1 != stone2:
                stones.append(stone1-stone2)
        if len(stones)==0:
            return 0
        else:
            return stones[0]