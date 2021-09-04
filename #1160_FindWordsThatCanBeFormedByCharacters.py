class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        hashmap = {}
        for c in chars:
            if c in hashmap:
                hashmap[c] += 1
            else:
                hashmap[c] = 1
        result = 0
        for word in words:
            count = 0
            for c_word in word:
                if c_word in hashmap:
                    if word.count(c_word) <= hashmap[c_word]:
                        count += 1
            if count == len(word):
                result += len(word)
        return result
