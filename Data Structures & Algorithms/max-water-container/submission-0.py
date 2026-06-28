class Solution:
    def maxArea(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        max_area = 0
        while l < r:
            small = 0
            if nums[l] < nums[r]:
                small = nums[l]
                l+=1
            else:
                small = nums[r]
                r-=1
            
            curr_stor = small*((r+1)-(l))
            max_area = max(max_area,curr_stor)
        return max_area


        