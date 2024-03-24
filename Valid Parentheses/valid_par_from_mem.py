class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        stk_map = { ']': '[', ')': '(', '{': '}',}

        # Loop through every character in the str
        for c in s:
           # if an open prn found  
           if c not in stk_map:
               # Push it to the stack
               stack.append(c)
               # Keep looping
               continue
           if not stack or stack[-1] != stack_map[c]
               return False
           stack.pop()

        return not stack
