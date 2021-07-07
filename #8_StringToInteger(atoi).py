class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        negative = False
        getsymbol = False
        number = ""
        if len(s) == 0:
            return 0
        else:
            # 1. Skip space and get the '-' or '+'
            while (s[0] == " " or s[0] == "+" or s[0] == "-") and not getsymbol:
                if s[0] == "-":
                    negative = True
                    getsymbol = True
                if s[0] == "+":
                    getsymbol = True
                if len(s) == 1:
                    break
                else:
                    s = s[1:]
            # 2. Record the number part
            while s[0].isdigit():
                number += s[0]
                if len(s) == 1:
                    break
                else:
                    s = s[1:]
            # 3. Convert string to integer
            result = int(number) if len(number) > 0 else 0
            result = min(result, 2 ** 31)
            return result * (-1) if negative else result




if __name__ == '__main__':
    solution = Solution()
    s = "-987.59856dfsdfafd4"
    r= solution.myAtoi(s)
    print(r)