class Solution:
    def simplifyPath(self, path: str) -> str:
        paths = [p for p in path.split("/") if p!="." or p!=""]
        stack = []

        for p in paths:
            if p == "..":
                if len(stack) > 0:
                    stack.pop()
            else:
                stack.append(p)

        return '/' + '/'.join(stack)
