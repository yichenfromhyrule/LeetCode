class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = ['(','[','{']
        right = [')',']','}']
        if len(s)%2 == 1:
            return False
        elif s[0] in right:
            return False
        elif len(s)==0:
            return True
        else:
            check = [s[0]]
            s = s[1:]
            while len(s)>0:
                c=s[0]
                if c in left:
                    check.append(c)
                    s = s[1:]
                elif c in right:
                    if len(check)==0:
                        return False
                    else:
                        check_last = check[len(check)-1]
                        if right.index(c) == left.index(check_last):
                            check.pop()
                            s = s[1:]
                        else:
                            return False
            if len(check)==0:
                return True
            else:
                return False


if __name__ == '__main__':
    s = Solution()
    roman = "(){}}{"
    r = s.isValid(roman)
    print(r)