class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        letters = [[],[],['a','b','c'],['d','e','f'],['g','h','i'],['j','k','l'],['m','n','o'],['p','q','r','s'],['t','u','v'],['w','x','y','z']]
        result = []
        if len(digits)==0:
            return result
        else:
            num_digits = 1
            for digit in digits:
                num_digits *= len(letters[int(digit)])
            result = ["" for i in range(num_digits)]
            x = num_digits
            for i in range(len(digits)):
                curr_letters = letters[int(digits[i])]
                x = x // len(curr_letters) #repeat times of a letter in the key
                y = num_digits // (len(curr_letters)*x)  # repeat times of a key
                #print("i = ",i," current letters = ",curr_letters, ", x = %d, y = %d"%(x,y))
                p=0
                for m in range(y):
                    for j in range(len(curr_letters)) :
                        for n in range(x):
                            result[p] += curr_letters[j]
                            p+=1
                #print(result)
            return result


if __name__ == '__main__':
    s = Solution()
    digits = "25"
    r = s.letterCombinations(digits)
    print(r)