class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        hashmap = {}
        index = 0
        for c in order:
            hashmap[c] = index
            index += 1

        l = len(words)
        if l == 1:
            return True
        else:
            for i in range(1, l):
                word_1 = words[i - 1]
                word_2 = words[i]
                if len(word_1) > len(word_2) and word_1[0:len(word_2)] == word_2:
                    return False
                else:
                    min_len = min(len(word_1), len(word_2))
                    for c1, c2 in zip(word_1[:min_len], word_2[:min_len]):
                        if hashmap[c1] > hashmap[c2]:
                            return False
                        if hashmap[c1] < hashmap[c2]:
                            break
            return True