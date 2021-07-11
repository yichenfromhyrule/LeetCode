class Solution(object):
    def countPalindromicSubsequence(self, s):
        """
        :type s: str
        :rtype: int
        """
        hashmap = {}
        for i in range(0, len(s)):
            if s[i] in hashmap:
                hashmap[s[i]].append(i)
            else:
                hashmap[s[i]] = [i]
        result = 0
        for key in hashmap:
            index_list = hashmap[key]
            if len(index_list) > 1:
                # 1. Only those size larger than 1 can become the start and end of the subsequence
                start = index_list[0]
                end = index_list[len(index_list)-1]
                # 1.a. Find unique character between [start:end]
                sub_result = self.findUnique(s, start, end)
                result += sub_result
                # 2. Add 1 as they can become start+mid+end
                result += 1 if len(hashmap[key]) >= 3 else 0
        return result
    def findUnique(self, s, start, end):
        sub_string = s[start:end]
        hashmap = {}
        result = 0
        for i in range(0, len(sub_string)):
            if sub_string[i] not in hashmap:
                hashmap[sub_string[i]] = i
                result += 1
        return result-1
if __name__ == '__main__':
    s = Solution()
    str = "bbcbaba"
    r = s.countPalindromicSubsequence(str)
    print(r)