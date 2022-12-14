class Solution:
    # TC: O(n^2logn), MC: O(n)
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}
        
        for i, word in enumerate(strs):
            sortedStr = sorted(word)
            joindStr = ''.join(sortedStr)
            if joindStr in dict:
                dict[joindStr].append(strs[i])
            else:
                dict[joindStr] = [strs[i]]
        values = dict.values()
        return list(values)
