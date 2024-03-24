from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []       

        for token in tokens:
            try:
                isinstance(int(token), int)
                stack.append(int(token))
            except ValueError:
                x = stack.pop()
                y = stack.pop()
                if token == '+':
                    res = y + x
                    stack.append(res)
                if token == '-':
                    res = y - x
                    stack.append(res)
                if token == '*':
                    res = y * x
                    stack.append(res)
                if token == '/':
                    res = int(y / x)
                    stack.append(res)
        return stack[-1]

soln = Solution()
tc_1 = ["2","1","+","3","*"]
tc_2 = ["4","13","5","/","+"]
tc_3 = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]

print(soln.evalRPN(tc_1))
print(soln.evalRPN(tc_2))
print(soln.evalRPN(tc_3))
