###############################################################################################
# 经典栈的应用
###########
# 时间复杂度：O(n)
# 空间复杂度：O(n)
###############################################################################################
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = {
            ']': '[',
            '}': '{',
            ')': '('
        }
        for c in s:
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            else:
                if stack and stack[-1] == dic[c]:
                    stack.pop()
                else:
                    return False
        if stack:
            return False
        return True