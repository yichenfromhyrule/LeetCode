class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_list = [c for c in s]
        t_list = [c for c in t]
        s_list.sort()
        t_list.sort()
        return s_list==t_list