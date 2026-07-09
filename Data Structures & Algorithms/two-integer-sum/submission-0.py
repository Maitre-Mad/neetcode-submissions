class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # create a hashmap (Correct)
        hashmap = {} 
        
        # go through the list and get index (i) and value (n) (Correct)
        for i, n in enumerate(nums):
            # complement of the target (Correct)
            diff = target - n 
            
            # if the complement is in the hashmap (Correct)
            if diff in hashmap:
                # ERROR HERE: You wrote [hashmap[i], i]
                # CONCEPT: You need the index of the DIFF, not the index of i.
                # FIX: return [hashmap[diff], i]
                return [hashmap[diff], i]
            
            else:
                # add the value (n) as the key and the index (i) as the value (Correct)
                hashmap[n] = i