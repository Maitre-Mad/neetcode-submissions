class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        tracker=[0]*26

        for i in range(len(s)):
            tracker[ord(s[i])-ord('a')]+=1
            tracker[ord(t[i])-ord('a')]-=1

        for count in tracker:
            if count!=0:
                return False
        
        return True