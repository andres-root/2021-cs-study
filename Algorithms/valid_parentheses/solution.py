class Solution:
    def isValid(self, s: str) -> bool:
        tags = {
            '(': ')',
            '[': ']',
            '{': '}'
        }
        
        if len(s) < 2 or tags.get(s[0]) == None:
            return False
        
        stack = []
        h = len(stack)
        
        for i, c in enumerate(s):
            if tags.get(c) == None and i > 0:
                if len(stack) == 0:
                    return False
                
                if c != stack[len(stack) - 1]:
                    return False
                
                stack.pop()
            else:
                stack.append(tags[c])
            
        return len(stack) == 0
