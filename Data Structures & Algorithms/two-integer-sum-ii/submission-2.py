class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = 1
        while left < len(numbers)-1:
            curr_sum = numbers[left] + numbers[right]
            if curr_sum == target:
                return [left+1,right+1]
            elif curr_sum < target :
                right+=1
            else:
                left+=1
                right = left+1
            if right > len(numbers)-1:
                left+=1
                right = left + 1
        

        