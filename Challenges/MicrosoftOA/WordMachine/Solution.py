# Doubtful


'''
an interger -- mahcine push the x onto the stack.
POP - machine remove the topmost number form the stack
DUP - the machine pushed the duplicate of the topmost no. of the stack.
+ - the machine addes the top two numbers and push it back.
- - The machine subs top - second top and push the result in back
'''

def wordProcess(type,stack):
    if type == "POP":
        if stack:
            stack.pop()
        return None
    else:
        return stack[-1] if stack else -1

def sign(signType,stack):
    if len(stack) < 2:
        return -1

    topFirst = stack.pop()
    topSecond = stack.pop()

    if signType == '+':
        return topFirst + topSecond
    return topFirst - topSecond

def processing(s):
    if s is None or len(s) == 0:
        return -1
    stack = []
    for word in s.split(' '):
        if word.isnumeric():
            stack.append(int(word))
        elif word in ["POP","DUP"]:
            res = wordProcess(word, stack)
            if res == -1:
                return -1
            else:
                if res is not None:
                    stack.append(res)
        else:
            res = sign(word,stack)
            if res == -1:
                return -1
            else:
                stack.append(res)
    return stack[-1]


s = "13 DUP 4 POP 5 DUP + DUP + -"
print(processing(s))

print(processing("5 6 + -"))
print(processing("3 DUP 5 - -"))