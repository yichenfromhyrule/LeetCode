class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if divisor == -1 and dividend == -1 * (2 ** 31):
            return (2 ** 31) - 1

        result = ""
        negative = True if (divisor < 0 and dividend >= 0) or (divisor >= 0 and dividend < 0) else False
        divisor = abs(divisor)
        dividend = abs(dividend)
        if divisor == 1:
            return (0 - dividend) if negative else dividend
        else:
            if dividend < divisor:
                return 0
            elif dividend == divisor:
                return -1 if negative else 1
            else:
                str_dividend = str(dividend)
                i = len(str(divisor))
                while int(str_dividend) >= divisor:
                    taken_dividend = str_dividend[:i]
                    print("1. taken_dividend is ", taken_dividend)
                    taken_int = int(taken_dividend)
                    while taken_int < divisor:
                        i += 1
                        taken_dividend = str_dividend[:i]
                        result += "0"
                        taken_int = int(taken_dividend)
                    print("2. current taken dividend is", taken_dividend, ", and divisor is ", divisor, "result is ", result)
                    taken_result = 0
                    while taken_int >= divisor:
                        taken_result += 1
                        taken_int -= divisor
                    result += str(taken_result)
                    str_dividend = str(taken_int) + str_dividend[i:]
                    i = len(str(taken_int))+1
                    print("3. current str_dividend is ", str_dividend, "current result is ", result)
                if len(result) < (len(str(dividend))-len(str(divisor))+1):
                    result += "0"*((len(str(dividend))-len(str(divisor))+1) - len(result))
                return int(result) * -1 if negative else int(result)

if __name__ == '__main__':
    s = Solution()
    x = -214
    n = -70
    print("correct answer: ", x/n)
    r = s.divide(x,n)
    print(r)