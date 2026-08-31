class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        Maxcount=0
        currentcount=0
        for num in nums:
            if num==1:


                currentcount+=1
            else:
                Maxcount= max(Maxcount,currentcount)
                currentcount=0
        return max(Maxcount,currentcount)
        
        