class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        maps = {}
        ans_list = []
        for i,s in enumerate(strs):
            s1 = sorted(s)
            j = i+1
            ans = []
            ans.append(s)
            for k in range(j,len(strs),1):
                if sorted(strs[k]) == s1:
                    ans.append(strs[k])
            s1 = tuple(s1)
            if maps.get(s1):
                continue
            maps[s1] = ans
        for a in maps.values():
            ans_list.append(a)
        return ans_list
