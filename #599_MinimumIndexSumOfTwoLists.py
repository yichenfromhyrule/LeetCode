class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        hashmap1 = {}
        for i in range(len(list1)):
            hashmap1[list1[i]] = i
        result = []
        index_sum = len(list1) + len(list2) - 2
        for j in range(len(list2)):
            if list2[j] in hashmap1:
                if (j + hashmap1[list2[j]]) < index_sum:
                    result = [list2[j]]
                    index_sum = j + hashmap1[list2[j]]
                elif (j + hashmap1[list2[j]]) == index_sum:
                    result.append(list2[j])
        return result
