class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        hashmap = [-1 for i in range(127)]
        result = 0
        left_key = 0
        if len(s)==0:
            return result
        else:
            longest = 0
            for i in range(0, len(s)):
                if hashmap[ord(s[i])]==-1 or hashmap[ord(s[i])]<left_key:
                    hashmap[ord(s[i])]=i
                    longest = i-left_key+1
                else:
                    if longest>result:
                        result = longest
                    left_key = hashmap[ord(s[i])]+1
                    hashmap[ord(s[i])] = i
                    longest = i-left_key+1
                print("current checking is %s, the longest is %d, the range is [%d,%d]."%(s[i],longest,left_key,i),s[left_key:i+1])
            return result if result>longest else longest
if __name__ == '__main__':
    s = Solution()
    str = "dagdkgaksgd"
    r = s.lengthOfLongestSubstring(str)
    print(r)