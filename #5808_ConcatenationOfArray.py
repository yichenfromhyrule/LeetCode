class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return nums + nums

if __name__ == '__main__':
    s = Solution()
    str = "dagdkgaksgd"
    r = s.lengthOfLongestSubstring(str)
    print(r)