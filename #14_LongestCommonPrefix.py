class Solution(object):
    def commonPrefix(self, str1, str2):
        result = ""
        min_len = min(len(str1), len(str2))
        if min_len == 0:
            return result
        else:
            str1 = str1[:min_len]
            str2 = str2[:min_len]
            for c1, c2 in zip(str1, str2):
                if c1==c2:
                    result+=c1
                else:
                    return result
            return result


    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 1:
            return strs[0]
        else:
            compare_str = strs[0]
            for i in range(1, len(strs)):
                current_str = strs[i]
                compare_str = self.commonPrefix(current_str, compare_str)
            return compare_str


if __name__ == '__main__':
    s = Solution()
    roman = ["flower","flow","flight"]
    r = s.longestCommonPrefix(roman)
    print(r)
