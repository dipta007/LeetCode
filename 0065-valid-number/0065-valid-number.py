class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.lower()

        def is_int(s, sign_possible=True):
            if len(s) == 0: return False
            if sign_possible:
                if s[0] == '+' or s[0] == '-':
                    s = s[1:]
                if len(s) == 0: return False
            for c in s:
                if not c.isnumeric():
                    return False
            return True

        def is_float(s):
            if len(s) == 0: return False
            if s[0] == '+' or s[0] == '-':
                s = s[1:]
            if len(s) == 0: return False
            floats = s.split('.')
            if len(floats) > 2: return False
            
            if len(floats) == 1:
                if not is_int(floats[0], sign_possible=False):
                    return False
            else:
                if len(floats[0]) > 0 and not is_int(floats[0], sign_possible=False):
                    return False
                if len(floats[1]) > 0 and not is_int(floats[1], sign_possible=False):
                    return False

                if len(floats[0]) == 0 and len(floats[1]) == 0:
                    return False
            
            return True

        # check if any other chars
        for c in s:
            if not c.isnumeric() and c not in ['e', '.', '+', '-']:
                return False
        
        exps = s.split("e")
        # if "e" more than once, 0 or 1 is okay
        if len(exps) > 2:
            return False

        if len(exps) > 0:
            print(is_int(exps[0]))
            print(is_float(exps[0]))
            print(exps)
        # if first one is not int and not float
        if not is_int(exps[0]) and not is_float(exps[0]):
            return False

        # if there is second, that much have to be int
        if len(exps) == 2:
            if not is_int(exps[1]):
                return False
        
        return True