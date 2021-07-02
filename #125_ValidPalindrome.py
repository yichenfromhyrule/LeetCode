class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        alnum_str = ""
        for c in s:
            if c.isalnum():
                alnum_str+=c
        alnum_str = alnum_str.lower()
        return alnum_str==alnum_str[::-1]
if __name__ == '__main__':
    s = Solution()
    str = "A man, a plan, a canal: Panama"
    r = s.isPalindrome(str)
    print(r)