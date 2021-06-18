class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        else:
            return x == int(str(x)[::-1])

if __name__ == '__main__':
    s = Solution()
    num = -10
    r = s.isPalindrome(num)
    print(r)