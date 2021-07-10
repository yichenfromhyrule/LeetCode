class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # 0. The result length is 2*n
        result_list = ['*' for i in range(n)]
        # 1. The first must be '(' and the last one must be ')'
        result_list[0] = '('
        result_list[len(result_list)-1] = ')'
        # 2. The question is converted to place the last n-1 '(' in 2n-2 place
        result = []
        


        return result

if __name__ == '__main__':
    s = Solution()
    n = 3
    r = s.generateParenthesis(n)
    print(r)