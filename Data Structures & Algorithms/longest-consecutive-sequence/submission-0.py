class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nn = list(set(nums))
        if len(nn)<=1:
            return len(nn)
        nn.sort()
        print(nn)
        curr = 0
        max_seq = 0
        for i in range(1,len(nn)):
            if nn[i] == nn[i-1] + 1:
                curr+=1
            else:
                max_seq = max(max_seq , curr)
                curr = 0
        max_seq = max(max_seq, curr)
        return max_seq + 1
        

        