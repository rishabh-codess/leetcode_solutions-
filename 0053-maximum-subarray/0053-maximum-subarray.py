class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
       currentSum=nums[0]
       maxSum=nums[0]

       for x in nums[1:]:
        currentSum=max(x,currentSum+x)
        maxSum=max(maxSum,currentSum)
       return maxSum
