class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        l = ""
        s = ""
        if len(a)>len(b):
            l = a
            s = b
        else:
            l = b
            s = a
        addOne = False
        r = ["0" for i in range(len(l))]
        for i in range(len(l)-1, -1, -1):
            index_s = len(s) - (len(l)-i)
            if index_s>=0:
                sum_i = int(l[i])+int(s[index_s])
                if sum_i==2:
                    r[i] = "1" if addOne else "0"
                    addOne=True
                elif sum_i==1:
                    r[i] = "0" if addOne else "1"
                else:
                    r[i] = "1" if addOne else "0"
                    addOne=False
            else:
                val_i = int(l[i])
                if val_i==0:
                    r[i] = "1" if addOne else "0"
                    addOne = False
                elif val_i==1:
                    r[i] = "0" if addOne else "1"
        if addOne:
            result = ["1"]+r
        else:
            result = r
        sum_r = ""
        for c in result:
            sum_r+=c
        return sum_r





if __name__ == '__main__':
    s = Solution()
    a = "10100"
    b = "10"
    r = s.addBinary(a,b)
    print(r)