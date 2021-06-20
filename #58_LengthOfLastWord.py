class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s_array = s.split(" ")
        #print(s_array)
        for i in range(len(s_array)-1,-1, -1):
            #print("Checking: ", i)
            if len(s_array[i]) > 0:
                return len(s_array[i])
        return 0

if __name__ == '__main__':
    s = Solution()
    str = "Hello World "
    r = s.lengthOfLastWord(str)
    print(r)