class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        start = 0
        end = len(s) - 1
        while start < end:
            if s[start] in vowels and s[end] in vowels:
                s = s[:start] + s[end] + s[start+1:end] + s[start] + s[end+1:]
                start += 1
                end -= 1
            else:
                if s[start] not in vowels:
                    start += 1
                if s[end] not in vowels:
                    end -= 1
        return s