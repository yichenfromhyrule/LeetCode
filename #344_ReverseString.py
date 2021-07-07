class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        # 1. len(s) is odd
        # 2. len(s) is even
        if len(s) % 2 == 1:
            mid = len(s) // 2
            left = mid - 1
            right = mid + 1
        else:
            mid_r = len(s) / 2
            mid_l = mid_r - 1
            temp = s[mid_l]
            s[mid_l] = s[mid_r]
            s[mid_r] = temp
            left = mid_l - 1
            right = mid_r + 1
        while left >= 0 and right < len(s):
            temp = s[left]
            s[left] = s[right]
            s[right] = temp
            left -= 1
            right += 1