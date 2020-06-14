'''
class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:
        def multi(s1, s2):
            ret = set()
            for v1 in s1:
                for v2 in s2:
                    ret.add(v1+v2)
            return ret
        q = collections.deque([])
        opstack = []
        i = 0
        rank = {
            "+": 0, 
            "*": 1
        }
        while i < len(expression):
            if ord("a") <= ord(expression[i]) <= ord("z"):
                if i > 0 and expression[i-1] == "}":
                    while opstack and opstack[-1] != "{" and rank[opstack[-1]] >= rank["*"]:
                        q.append(opstack.pop())
                    opstack.append("*")
                val = ""
                while i < len(expression) and ord("a") <= ord(expression[i]) <= ord("z"):
                    val += expression[i]
                    i += 1
                q.append(val)
            elif expression[i] in {"{", ","}:
                if expression[i] == "{":
                    op = "*"
                else:
                    op = "+"
                while opstack and opstack[-1] != "{" and rank[opstack[-1]] >= rank[op]:
                    q.append(opstack.pop())
                if expression[i] == ",":
                    opstack.append("+")
                else:
                    if i > 0 and (expression[i-1] == "}" or ord("a") <= ord(expression[i-1]) <= ord("z") ):
                        opstack.append("*")
                    opstack.append("{")
                i += 1
            elif expression[i] == "}":
                while opstack and opstack[-1] != "{":
                    q.append(opstack.pop())
                opstack.pop()
                i += 1
            else:
                i += 1
        numstack = []
        while opstack:
            q.append(opstack.pop())
        for op in q:
            if op in {"+", "*"}:
                v2 = numstack.pop()
                v1 = numstack.pop()
                if op == "+":
                    numstack.append(v1|v2)
                else:
                    numstack.append(multi(v1, v2))
            else:
                numstack.append(set([op]))
        return sorted(numstack[0])
'''