class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        
        count_S={}
        count_T={}
        for character in s:
            count_S[character]=count_S.get(character,0)+1
        for character in t:
            count_T[character]=count_T.get(character,0)+1
        
        return count_S==count_T