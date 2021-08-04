###############################################################################################
# 这道题很难想，没想到能用O(n)的方法，栈里存放的不是'('，而是其下标；实际上，该算法保持了栈底永远是前一个没有被匹配的')'的下标
# 因此初始化')'的下标就是-1；且之后仅放入'('的下标，每次来了')直接pop，如果不为空，说明栈底的')'没有被pop掉，说明匹配成功
# 此时最大长度就是当前')'的下标减去栈顶'('的下标，这样就让没有被匹配的'('和前一个没有匹配的')'起到了隔断作用，成功记录最大长度
###########
# 时间复杂度：O(n)
# 空间复杂度：O(n)
###############################################################################################
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        len_, res = len(s), 0
        stack = [-1]

        for i in range(len_):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if stack:
                    res = max(res, i - stack[-1])
                else:
                    stack.append(i)

        return res


###############################################################################################
# 神他妈的动规，我不是没想过，想过区间、一维线性，甚至就是以i结尾的最长长度，但是在想转移的时候，只想到一半
# 也真的没想到，动规一维居然能做出来，本以为没法转移
# 不过dp确实比前面那个栈更好理解
###########
# 时间复杂度：O(n)
# 空间复杂度：O(n)
###############################################################################################
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        len_, res = len(s), 0
        dp = [0]*len_ # dp[i]: 以i结尾的最长合法括号子串长度

        for i in range(1, len_):
            if s[i] == ')':
                if s[i-1] == '(':
                    dp[i] = 2 if i-2 < 0 else 2 + dp[i-2]
                elif i - dp[i-1] - 1 >= 0 and s[i-dp[i-1]-1] == '(': # 即s[i-1] == '('，这是最精妙的部分，神了
                    dp[i] = dp[i-1] + 2 + (dp[i-dp[i-1]-2] if i-dp[i-1]-2 >= 0 else 0)
                res = max(res, dp[i])

        return res

###############################################################################################
# 虽然没解出此题，但官方给的这三种方法：栈、dp、记左右括号，我都想过！！但没一道完整地想出来
# 不过还是能说明我的题感提高了很多哈
# 这种记录left和right的做法，right的隔断很简单，left right都归0就行了，但left 一直 大于 right的情况却没办法，一开始就是卡在这里！
# 官方给出的解决方案竟然是：从右往左遍历就好了。我真是人没了，这样其实就反过来了，left多的相当于之前的right隔断，此时right 大于 left的没法统计
# 因此，从左往右，从右往左 各来一次！！！我直呼好家伙
###########
# 时间复杂度：O(n)
# 空间复杂度：O(1)
###############################################################################################
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        len_, res = len(s), 0
        l = r = 0
        for i in range(len_):
            if s[i] == '(':
                l += 1
            else:
                r += 1
            if l == r:
                res = max(res, l+r)
            if r > l: # 这是隔断的地方
                l = r = 0
        l = r = 0
        for i in range(len_-1, -1, -1):
            if s[i] == ')':
                r += 1
            else:
                l += 1
            if l == r:
                res = max(res, l+r)
            if l > r: # 这是从右往左隔断的地方
                l = r = 0
        return res

# 写一个循环也可以
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        len_, res = len(s), 0
        l1 = r1 = l2 = r2 = 0
        for i in range(len_):
            j = len_ - i - 1 # 反着来
            if s[i] == '(':
                l1 += 1
            else:
                r1 += 1
            if l1 == r1:
                res = max(res, l1+r1)
            if r1 > l1: # 这是左往右隔断的地方
                l1 = r1 = 0
            
            if s[j] == '(':
                l2 += 1
            else:
                r2 += 1
            if l2 == r2:
                res = max(res, l2+r2)
            if l2 > r2: # 这是从右往左隔断的地方
                l2 = r2 = 0
            
        return res