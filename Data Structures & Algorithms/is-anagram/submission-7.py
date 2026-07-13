class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        
        counter_s={}
        counter_t={}

        for character in s:
            counter_s[character]=counter_s.get(character,0)+1
        for character in t:
            counter_t[character]=counter_t.get(character,0)+1
        
        return counter_s==counter_t