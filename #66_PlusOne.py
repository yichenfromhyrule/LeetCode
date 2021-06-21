class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        addOne = True
        for i in range(len(digits)-1, -1, -1):
            if addOne==True and digits[i]!=9:
                digits[i]+=1
                return digits
            if addOne==True and digits[i]==9:
                digits[i]=0
        if addOne:
            return [1]+digits

if __name__ == '__main__':
    s = Solution()
    str = [0]
    r = s.plusOne(str)
    print(r)