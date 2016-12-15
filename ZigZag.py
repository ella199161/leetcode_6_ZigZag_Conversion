class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows<=1:
            return s
        res=''    
        res=s
        n=len(s)
        k=0
        for i in range(numRows):
            for j in range(1,n,2*(numRows-1)):
                res[k]= s[j]
                k=k+1
                if i>0 and i< numRows-1 and j+2*(numRows-1-i)<n:
                    res[k]=s[j+2*(numRows-1-i)]
                    k=k+1
        return res
