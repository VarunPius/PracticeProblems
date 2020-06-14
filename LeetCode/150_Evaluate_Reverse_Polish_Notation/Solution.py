ops = {
    "+" : (lambda a, b : b + a),
    "-" : (lambda a, b : b - a),
    "/" : (lambda a, b : int(b / a)),
    "*" : (lambda a, b : b * a)
}

class Solution:
    #This method uses LL and LR Parsing
    def evalRPN(self, tokens) -> int: #evalRPN(self, tokens: List[str])
        result = 0
        operator = "+-/*"
        stack = []
        for token in tokens:
            print(token)
            if token not in operator:
                stack.append(int(token))
            else:
                num1 = stack.pop()
                num2 = stack.pop()
                calc = ops[token](num1, num2)
                stack.append(calc)
        result = stack.pop()
        return result

    #case method; python doesnt have switch case
    def evalRPN2(self, tokens) -> int: #evalRPN(self, tokens: List[str])
        result = 0
        operator = "+-/*"
        stack = []
        for token in tokens:
            print(token)
            if token not in operator:
                stack.append(int(token))
            else:
                num1 = stack.pop()
                num2 = stack.pop()
                if token == "+":
                    calc = num2 + num1
                elif token == "-":
                    calc = num2 - num1
                elif token == "/":
                    calc = int(num2 / num1)
                elif token == "*":
                    calc = num2 * num1
                stack.append(calc)
        result = stack.pop()
        return result

def main():
    soln = Solution()
    result = soln.evalRPN(["4", "10", "5", "/", "+"])
    print(result)

if __name__ == "__main__":
    main()

