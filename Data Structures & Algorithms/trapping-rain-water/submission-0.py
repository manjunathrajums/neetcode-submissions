class Solution:
    def trap(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) -1
        ans = 0
        lmax = nums[l]
        rmax = nums[r]
        while l < r:
            if lmax < rmax :
                ans += lmax - nums[l]
                l+=1
                lmax = max(lmax,nums[l])
            else:
                ans += rmax - nums[r]
                r-=1
                rmax = max(rmax,nums[r])
        return ans
        


