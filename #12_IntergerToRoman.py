class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        symbol_list = [['I','V'],['X','L'],['C','D'],['M','N']] # N will never be used
        num_str = str(num)[::-1]
        result = ""
        for i in range(0, len(num_str)):
            symbol_sublist = symbol_list[i]
            integer = int(num_str[i])
            if integer <= 3:
                symbol = symbol_sublist[0] * integer
            elif integer == 4:
                symbol = symbol_sublist[0] + symbol_sublist[1]
            elif integer < 9:
                symbol = symbol_sublist[1] + symbol_sublist[0] * (integer - 5)
            elif integer == 9:
                symbol_nextlist = symbol_list[i+1]
                symbol = symbol_sublist[0] + symbol_nextlist[0]
            result = symbol + result
        return result

if __name__ == '__main__':
    solution = Solution()
    num = 1994
    r= solution.intToRoman(num)
    print(r)