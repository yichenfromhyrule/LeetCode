class Solution(object):
    def checkHappy(self,n,result_list):
        string_n = str(n)
        r = 0
        for c in string_n:
            r += int(c) ** 2

        if r == 1:
            return True
        else:
            if r in result_list:
                return False
            else:
                result_list.append(r)
                return self.checkHappy(r,result_list)
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        result_list = []
        r = self.checkHappy(n, result_list)
        return r

if __name__ == '__main__':
    s = Solution()
    n = 19
    r = s.isHappy(n)
    print(r)