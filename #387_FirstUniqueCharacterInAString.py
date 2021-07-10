class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 1. Create a hashmap that the character's ascii value as index
        hashmap = [-1 for j in range(123)]
        # 2. Go through the string and add 1 in the hashmap once the character appears
        for c in s:
            hashmap[ord(c)] += 1
        # 3. Go through the string and return the character hashmap value is 0
        for i in range(0, len(s)):
            if hashmap[ord(s[i])] == 0:
                return i
        return -1

if __name__ == '__main__':
    solution = Solution()
    s = "leelllll"
    r = solution.firstUniqChar(s)
    print(r)