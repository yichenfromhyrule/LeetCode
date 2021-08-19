class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        five = 0
        ten = 0
        for bill in bills:
            charge = bill - 5
            if charge == 0:
                five += 1
            elif charge == 5:
                if five > 0:
                    five -= 1
                    ten += 1
                else:
                    return False
            elif charge == 15:
                if ten > 0 and five > 0:
                    ten -= 1
                    five -= 1
                elif five > 2:
                    five -= 3
                else:
                    return False
            print(five, ten)
        return True