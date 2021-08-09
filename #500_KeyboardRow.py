class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        rows = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
        result = []
        hashmap = {}
        for i in range(len(rows)):
            for c in rows[i]:
                hashmap[c] = i
        for word in words:
            word_l = word.lower()
            r_word = []
            for c_word in word_l:
                r_word.append(hashmap[c_word])
            if len(set(r_word)) == 1:
                result.append(word)
        return result
