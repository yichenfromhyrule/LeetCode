class Solution(object):
    def distanceBetweenBusStops(self, distance, start, destination):
        """
        :type distance: List[int]
        :type start: int
        :type destination: int
        :rtype: int
        """
        s = min(start,destination)
        d = max(start,destination)
        l1 = distance[s:d]
        l2 = distance[d:] + distance[:s]
        return min(sum(l1), sum(l2))