class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicate=[]
        for number in nums:
            if number in duplicate:
                return True
            duplicate.append(number)
        return False