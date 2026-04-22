# https://neetcode.io/problems/evaluate-reverse-polish-notation
class Solution:
    '''
    ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    Output: 22
    Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
    = ((10 * (6 / (12 * -11))) + 17) + 5
    = ((10 * (6 / -132)) + 17) + 5
    = ((10 * 0) + 17) + 5
    = (0 + 17) + 5
    = 17 + 5
    = 22
    '''
    # It doe pick up the last two for the operation
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ['+', '-', '*', '/']
        operands = [] # can be more than 2, 3 4 + 5 6 + × : (3+4) * (5+6)
        result = 0
        for t in tokens:
            if t in operators:
                if len(operands) < 2:
                    raise ValueError('Arithmatic operation requires 2 operands')
                second = operands.pop()
                first = operands.pop()
                match t:
                    case '+':
                        result = first + second
                    case '-':
                        result = first - second
                    case '*':
                        result = first * second
                    case _:
                        result = first // second
                        # This is an outliner throwing the number off
                        # -7 // 2 = -4, it truncates toward zero, it should be -3 instead
                        # Only apply for the above scenario. DO NOT apply for -6 // 2
                        if result < 0 and (first % second) != 0:
                            result += 1

                operands.append(result)
            else:
                try:
                    num = int(t)
                except:
                    raise ValueError('The operand need to be integer in these mathematical operations')
                operands.append(num)
        # In a normal operation, operands should be empty. The second scenario only happen if tokens has one token (num)
        return result if not operands else operands[-1]