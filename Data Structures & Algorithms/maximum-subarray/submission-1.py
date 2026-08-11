class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        submax = nums[0]
        cursum = 0
        for n in range(len(nums)):
            if cursum < 0:
                cursum =0
            cursum +=nums[n]
            submax = max(submax,cursum)
        return submax