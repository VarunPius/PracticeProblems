class Solution:
    # def braceExpansionII(self, expression: str) -> List[str]:
    def braceExpansionII(self, expression: str):
        return


'''
###############################################################################################
Python3 Clear and Short Recursive Solution
The general idea

Split expressions into groups separated by top level ','; for each top-level sub expression (substrings with braces), process it and add it to the corresponding group; finally combine the groups and sort.

Thought process

    in each call of the function, try to remove one level of braces
    maintain a list of groups separated by top level ','
        when meets ',': create a new empty group as the current group
        when meets '{': check whether current level is 0, if so, record the starting index of the sub expression;
            always increase level by 1, no matter whether current level is 0
        when meets '}': decrease level by 1; then check whether current level is 0, if so, recursively call braceExpansionII to get the set of words from expresion[start: end], where end is the current index (exclusive).
            add the expanded word set to the current group
        when meets a letter: check whether the current level is 0, if so, add [letter] to the current group
        base case: when there is no brace in the expression.
    finally, after processing all sub expressions and collect all groups (seperated by ','), we initialize an empty word_set, and then iterate through all groups
        for each group, find the product of the elements inside this group
        compute the union of all groups
    sort and return
    note that itertools.product(*group) returns an iterator of tuples of characters, so we use''.join() to convert them to strings

class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:
        groups = [[]]
        level = 0
        for i, c in enumerate(expression):
            if c == '{':
                if level == 0:
                    start = i+1
                level += 1
            elif c == '}':
                level -= 1
                if level == 0:
                    groups[-1].append(self.braceExpansionII(expression[start:i]))
            elif c == ',' and level == 0:
                groups.append([])
            elif level == 0:
                groups[-1].append([c])
        word_set = set()
        for group in groups:
            word_set |= set(map(''.join, itertools.product(*group)))
        return sorted(word_set)

###############################################################################################

Python concise stack solution
Use stack for "{" and "}" just like in calculator.
Maintain two lists:

    the previous list before ",",
    the current list that is still growing.

When seeing an "alphabet", grow the second list by corss multiplying. So that [a]*b will become "ab", [a,c]*b will become ["ab", "cb"]
When seeing ",", that means the second list can't grow anymore. combine it with the first list and clear the second list.
When seeing "{", push the two lists into stack,
When seeing "}", pop the previous two lists, cross multiplying the result inside "{ }" into the second list.

If not considering the final sorting before return, the time complexity should be O(n)

class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:
        stack,res,cur=[],[],[]
        for i in range(len(expression)):
            v=expression[i]
            if v.isalpha():
                cur=[c+v for c in cur or ['']]
            elif v=='{':
                stack.append(res)
                stack.append(cur)
                res,cur=[],[]
            elif v=='}':
                pre=stack.pop()
                preRes=stack.pop()
                cur=[p+c for c in res+cur for p in pre or ['']]
                res=preRes
            elif v==',':
                res+=cur
                cur=[]
        return sorted(set(res+cur))


###############################################################################################
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