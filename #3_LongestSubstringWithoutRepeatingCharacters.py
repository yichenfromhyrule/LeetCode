class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        hashmap = {} # Dictionary is better
        startkey = 0
        result = 0
        for i in range(0, len(s)):
            if s[i] in hashmap and hashmap[s[i]] >= startkey:
                # Which means this character already be checked
                result = max(result, i-startkey)
                startkey = hashmap[s[i]] + 1
            hashmap[s[i]] = i
        return max(result, len(s)-startkey)
if __name__ == '__main__':
    s = Solution()
    str = "dagdkgaksgd"
    r = s.lengthOfLongestSubstring(str)
    print(r)