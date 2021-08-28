class Solution(object):
    def diStringMatch(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        smallest = 0
        largest = len(s)
        result = []
        for c in s:
            if c == 'D':
                result.append(largest)
                largest -= 1
            else:
                result.append(smallest)
                smallest += 1
        return result + [smallest]