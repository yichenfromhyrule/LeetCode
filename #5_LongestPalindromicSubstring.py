class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s)==1:
            return s
        elif len(s)==2:
            return s if s[0]==s[1] else s[0]
        else:
        # 1. Need to find the "middle" character in the string
            result = ""
            for i in range(1,len(s)-1):
                m = i-1
                n = i+1
                if s[m]==s[n]: #2.a. It can be the middle character
                    a = m
                    b = n
                    while s[a]==s[b]:
                        print("current a = %d, b = %d, result = %s"%(a,b,result))
                        if a-1>=0 and b+1<len(s):
                            a-=1
                            b+=1
                        else:
                            break
                    palindormic_string = s[m:n+1]
                    result = palindormic_string if len(palindormic_string)>len(result) else result
        return result


if __name__ == '__main__':
    s = Solution()
    str = "cbbd"
    r = s.longestPalindrome(str)
    print(r)