class Solution:
    # TC: O(n), MC: O(n)
    def isAnagram(self, s: str, t: str) -> bool:
        volumeCountForS = {}

        for i in range(len(s)):
            if s[i] not in volumeCountForS:
                volumeCountForS[s[i]] = 1
            else:
                volumeCountForS[s[i]] += 1
        for i in range(len(t)):
            if t[i] not in volumeCountForS:
                return False
            else:
                if volumeCountForS[t[i]]>1:
                    volumeCountForS[t[i]] -= 1
                else:
                    del volumeCountForS[t[i]]
        
        return len(volumeCountForS)==0
