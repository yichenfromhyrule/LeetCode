class Solution(object):
    def numberOfLines(self, widths, s):
        """
        :type widths: List[int]
        :type s: str
        :rtype: List[int]
        """
        sum_pixels = 0
        rows = 1
        for c in s:
            if sum_pixels + widths[ord(c) - 97] <= 100:
                sum_pixels += widths[ord(c) - 97]
            else:
                rows += 1
                sum_pixels = widths[ord(c) - 97]
        return [rows, sum_pixels]