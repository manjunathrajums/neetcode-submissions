class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre_prod = []
        prod  = 1
        for num in nums:
            prod*=num
            pre_prod.append(prod)
        post_prod = []
        prod =1
        for i in range(len(nums)-1,-1,-1):
            prod*=nums[i]
            post_prod.append(prod)
        post_prod.reverse()
        ans =[]
        for i in range(len(nums)):
            if i==0:
                ans.append(post_prod[1])
            elif i == len(nums)-1:
                ans.append(pre_prod[len(nums)-2])
            else:
                ans.append(pre_prod[i-1]*post_prod[i+1])
        return ans



            
           

        