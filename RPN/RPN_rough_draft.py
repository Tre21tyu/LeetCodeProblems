from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        num_stack = []       
        ops_stack = []

        # Create two stacks
        for token in tokens:
            try:
                isinstance(int(token), int)
                num_stack.append(token)
            except ValueError:
                # num_stack.append("err")
                ops_stack = [token] + ops_stack

        i = len(num_stack)
        print(tokens)
        print("------------------")
        while i > 1:
            if ops_stack:
                print(num_stack, ops_stack)
                x = num_stack.pop()
                y = num_stack.pop()
                op = ops_stack.pop()
                res = 0
                print(f'Popped {x} and {y}, from the stack')
                print(f'New stack -> {num_stack} {ops_stack}')

                if op == '+':
                    res = int(y) + int(x)
                    print("found addition!")
                    print(f'{y} + {x} = {res}. pushing {res} to the stack')
                    num_stack.append(str(res))
                    i -= 1
                if op == '-':
                    res = int(y) - int(x)
                    print("Found Subtraction!")
                    print(f'{y} - {x} = {res} Pushing {res} to the stack')
                    num_stack.append(str(res))
                    i -= 1
                if op == '*':
                    res = int(y) * int(x)
                    print("Found Multiplication!")
                    print(f'{y} * {x} = {res} Pushing {res} to the stack')
                    num_stack.append(str(res))
                    i -= 1
                if op == '/':
                    print(f'x: {x}, y: {y}')
                    # res = int(y) // int(x)
                    res = int(int(y) / int(x))
                    print("Found Division!")
                    print(f'{y} // {x}  = {res} Pushing {res} to the stack')
                    num_stack.append(str(res))
                    i -= 1
            # print(i)
            # print(res)
            # print(num_stack)
            # print(ops_stack)
        # return num_stack, ops_stack
        return res



soln = Solution()
tc_1 = ["2","1","+","3","*"]
tc_2 = ["4","13","5","/","+"]
tc_3 = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]

print(soln.evalRPN(tc_1))
print(soln.evalRPN(tc_2))
print(soln.evalRPN(tc_3))
