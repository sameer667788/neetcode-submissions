class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n,res = len(nums),0
        c = 0
        for i in range(n):
            if nums[i] == 1:
                c += 1
                res = max(res, c)
            else:
                c = 0
        return res