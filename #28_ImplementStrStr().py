class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle)==0:
            return 0
        elif len(needle)>len(haystack):
            return -1
        else:
            for i in range(0, len(haystack)-len(needle)+1):
                if haystack[i]==needle[0]:
                    if haystack[i: i+len(needle)]==needle:
                        return i
            return -1


if __name__ == '__main__':
    s = Solution()
    h = "ah"
    n = "h"
    r = s.strStr(h,n)
    print(r)