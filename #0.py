class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        """
        :type text: str
        :type brokenLetters: str
        :rtype: int
        """
        hashmap = {}
        for letter in brokenLetters:
            hashmap[letter] = True
        text_array = text.split(" ")
        count = 0
        for text_item in text_array:
            broken = False
            for char_item in text_item:
                if char_item in hashmap:
                    broken = True
            count += 1 if not broken else 0
        return count

if __name__ == '__main__':
    s = Solution()
    text = "hello world"
    brokenLetters = "ad"
    r= s.canBeTypedWords(text, brokenLetters)
    print(r)