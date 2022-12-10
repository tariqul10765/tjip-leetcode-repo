class Solution:
    # TC: O(n), MC: O(n)
    def isValid(self, s: str) -> bool:
        stack=[]
        for i in s:
            if i=='(' or i=='{' or i=='[':
                stack.append(i)
            
            elif i==')':
                if len(stack) and stack[len(stack)-1]=='(':
                    stack.pop()
                else:
                    return False
            elif i=='}':
                if len(stack) and stack[len(stack)-1]=='{':
                    stack.pop()
                else:
                    return False
            elif i==']':
                if len(stack) and stack[len(stack)-1]=='[':
                    stack.pop()
                else:
                    return False
        if len(stack):
            return False
        return True
