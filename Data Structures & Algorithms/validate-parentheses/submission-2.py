class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        ex_map = {'}':'{', ']':'[', ')':'('}
        for i in s:
            if (i == '[') or (i == '{') or (i == '('):
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                elif (stack[len(stack)-1] == ex_map[i]):
                    stack.pop()
                else:
                    return False
        if len(stack) != 0:
            return False
        else:
            return True
            
            