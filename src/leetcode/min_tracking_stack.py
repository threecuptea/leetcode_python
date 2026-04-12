# https://www.hackerrank.com/contests/software-engineer-prep-kit/challenges/min-tracking-stack
def processCouponStackOperations(operations):
    # Write your code here
    stack, result, min_nums = [], [], []
    for op in operations:
        match op:
            case "pop":
                item = stack.pop()
                if item == min_nums[-1]:
                    min_nums.pop()
            case "top":
                result.append(stack[-1])
            case "getMin":
                result.append(min_nums[-1])
            case _:
                num = int(op.split()[1])
                stack.append(num)
                # need equal here because 0 can be pushed multiple time
                if not min_nums or num <= min_nums[-1]:
                    min_nums.append(num)

    return result