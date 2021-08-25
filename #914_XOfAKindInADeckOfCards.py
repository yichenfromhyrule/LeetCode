class Solution(object):
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        if len(deck) <= 1:
            return False
        else:
            hashmap = {}
            for card in deck:
                if card not in hashmap:
                    hashmap[card] = 1
                else:
                    hashmap[card] += 1
            count_list = list(hashmap.values())
            count_list = list(set(count_list))
            count_list.sort()
            for i in range(count_list[0], 1, -1):
                flag = True
                for count in count_list:
                    if count % i != 0:
                        flag = False
                if flag:
                    return True
            return False