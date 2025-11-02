class Solution(object):
    def twoSum(self, n, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hp={}
        for i,n in enumerate(n):
            c=target-n
            if c in hp:
                return[hp[c],i]
            hp[n]=i    
        