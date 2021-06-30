class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = [[],["()"],["()()","(())"]]
        if n<=2:
            return result[n]
        else:
            for i in range(3,n+1):
                pre_list = result[i-1]
                curr_list = []
                for pre_Parenthesis in pre_list:
                    curr_Parenthesis = pre_Parenthesis + "()"
                    if curr_Parenthesis not in curr_list:
                        curr_list.append(curr_Parenthesis)
                    curr_Parenthesis = "()" + pre_Parenthesis
                    if curr_Parenthesis not in curr_list:
                        curr_list.append(curr_Parenthesis)
                    curr_Parenthesis = "(" + pre_Parenthesis + ")"
                    if curr_Parenthesis not in curr_list:
                        curr_list.append(curr_Parenthesis)
                result.append(curr_list)
            return result[n]

if __name__ == '__main__':
    s = Solution()
    n = 3
    r = s.generateParenthesis(n)
    print(r)