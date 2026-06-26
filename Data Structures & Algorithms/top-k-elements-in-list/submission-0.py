from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        f_map = Counter(nums)
        ans_list = []
        while k:
            n1 = max(f_map.values())
            for x,y in f_map.items():
                if y == n1:
                    f_map[x] = 0
                    ans_list.append(x)
                    break
            k-=1
        return ans_list


        
        