class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        curr_max = max(candies)
        at_least = curr_max - extraCandies
        result = []
        for candy in candies:
            if candy >= at_least:
                result.append(1)
            else:
                result.append(0)
        return result