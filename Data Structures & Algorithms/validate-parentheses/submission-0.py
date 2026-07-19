class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        bracket_map={'(': ')', '{':'}' , '[':']'}

        for character in s:
            if character in bracket_map:
                stack.append(bracket_map[character])
            else:
                if not stack or stack.pop() != character:
                    return False
        
        return len(stack)==0 