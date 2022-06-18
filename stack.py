class Solution:
    def isValid(self, s: str) -> bool:
        # thought process
        # ([]) is true
        # [(]) is false, weird 
        # add beginnings to stack
        # if see endings, then remove beginning
      
        stack = []
        dict = {"]":"[", "}":"{", ")":"("}
        for char in s:
            if char in dict.values():
                stack.append(char)
            elif char in dict.keys():
                if stack == [] or dict[char] != stack.pop():
                    return False
            else:
                return False
        return stack == []