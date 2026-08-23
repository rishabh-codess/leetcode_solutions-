class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        strs.sort()

        first = strs[0]
        last = strs[-1]
        p1 = 0
        p2 = 0

        while p1 < len(first) and p2 < len(last):
            if first[p1] == last[p2]:
                p1 += 1
                p2 += 1
            else:
                break

        return first[:p1]
         
        