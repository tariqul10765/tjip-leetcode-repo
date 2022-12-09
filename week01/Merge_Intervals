class Solution:
    # TC: O(nlogn), MC: O(n)
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        fst = intervals[0][0]
        last = intervals[0][1]
        
        res = []
        
        for i in range(1,len(intervals)):
            if intervals[i][0]<=last and intervals[i][0]>=fst:
                last = max(intervals[i][1],last)
            else:
                res.append([fst,last])
                fst = intervals[i][0]
                last = intervals[i][1]
        res.append([fst,last])
        return res
            
            
