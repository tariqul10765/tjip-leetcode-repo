class Solution:
    # TC: O(n^2), MC: O(n)
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==1:
            return strs[0]
        prefix = []
        k = 0

        minL = min(strs, key=len)

        for i in range(len(minL)):
            count = 1
            for j in range(len(strs)-1):
                if strs[j][i] == strs[j+1][i]:
                    count += 1
            if count != len(strs):
                if i != k:
                    prefix.append(strs[j][k:i])
                k = i+1

        if len(prefix) == 0:
            return ""
        return min(prefix, key=len)
