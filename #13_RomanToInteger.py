class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = ['I','V','X','L','C','D','M']
        number = [1,5,10,50,100,500,1000]
        value = 0
        for i in range(0, len(s)):
            c = s[i]
            c_index = roman.index(c)
            c_value = number[c_index]
            if (i<len(s)-1):
                next_index = roman.index(s[i+1])
                if c_index<next_index:
                    value-=c_value
                else:
                    value+=c_value
            else:
                value+=c_value
        return value
if __name__ == '__main__':
    s = Solution()
    roman = "MCMXCIV"
    r = s.romanToInt(roman)
    print(r)
