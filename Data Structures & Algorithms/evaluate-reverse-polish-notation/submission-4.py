class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == '+':
                second_num = stack.pop()
                first_num = stack.pop()
                stack.append(first_num + second_num)
            elif token == '-':
                second_num = stack.pop()
                first_num = stack.pop()
                stack.append(first_num - second_num)
            elif token == '*':
                second_num = stack.pop()
                first_num = stack.pop()
                stack.append(first_num * second_num)
            elif token == '/':
                second_num = stack.pop()
                first_num = stack.pop()
                stack.append(int(first_num / second_num))
            else:
                stack.append(int(token))
            
        return stack.pop()