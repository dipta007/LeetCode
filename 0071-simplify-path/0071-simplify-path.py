class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        paths = path.split("/")
        for p in paths:
            if p == '..':
                if len(stack):
                    stack.pop()
            elif p == '.' or not p:
                continue
            else:
                stack.append(p)

        path = "/".join(stack)

        if len(path) == 0 or path[0] != '/':
            path = "/" + path

        return path