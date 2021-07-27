class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        # 1. save each character's position in a hashmap
        hashmap = {}
        for y in range(0, len(board)):
            for x in range(0, len(board[0])):
                if board[y][x] in hashmap:
                    hashmap[board[y][x]].append([y, x])
                else:
                    hashmap[board[y][x]] = [[y, x]]

        for word_char in word:
            if word_char not in hashmap:
                return False
        paths = [[index] for index in hashmap[word[0]]]
        word = word[1:]
        while len(word) > 0:
            len_paths = len(paths)
            if len_paths == 0:
                return False
            checking, word = word[0], word[1:]
            for i in range(0, len_paths):
                for checking_index in hashmap[checking]:
                    target = paths[i][-1]
                    distance = abs(checking_index[0] - target[0]) + abs(checking_index[1] - target[1])
                    if distance == 1 and checking_index not in paths[i]:
                        paths.append(paths[i] + [checking_index])
            paths = paths[len_paths:]

        if len(paths) > 0:
            return True



