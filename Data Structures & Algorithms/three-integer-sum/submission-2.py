from collections import Counter
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []

        for i in range(len(nums)-2):
            if i>0 and nums[i] == nums[i-1]:
                continue
            l = i+1
            r = len(nums) - 1
            while l < r:
                sums = nums[i] + nums[l] + nums[r]
                if  sums == 0:
                    if [nums[i],nums[l],nums[r]] in ans:
                        pass    
                    else:
                        ans.append([nums[i],nums[l],nums[r]])
                    l+=1
                    r-=1
                elif sums < 0:
                    l+=1
                else:
                    r-=1
        return ans
                

        