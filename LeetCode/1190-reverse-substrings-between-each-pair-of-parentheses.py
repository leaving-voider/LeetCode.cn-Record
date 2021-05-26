###############################################################################################
# 利用栈，string存储当前层的字符串
###########
# 时间复杂度：O(n²)，n 是数组 s 的长度，每一次循环进行的字符串反转占n的时间复杂度
# 空间复杂度：O(n)，栈和字符串的消耗
###############################################################################################
class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = [] # 列表模拟栈
        string = ""

        for per in s:
            if per == '(': # 进入下一层，则当前层的string进入栈，string置空
                stack.append(string) # 可能是个空串
                string = ""
            elif per == ')': # 处理当前层的串
                string = string[::-1] # 先反转
                string = stack.pop() + string # 栈顶弹出前一层的并拼接
            else:
                string += per

        return string

###############################################################################################
# 官网给的启发，我称之为“向左向右”算法，每遇到一个左或右括号，就跳到对应的括号，且移动方向转变一次，继续遍历
# 只需要提前计算辅助函数，即对应括号的位置
###########
# 时间复杂度：O(n)，预处理出括号的对应关系的序列的时间复杂度为 O(n)，遍历字符串的时间复杂度同样为 O(n)
# 空间复杂度：O(n)，辅助数组和栈的消耗
###############################################################################################
class Solution:
    def reverseParentheses(self, s: str) -> str:
        len_ = len(s)
        cor = [-1]*len_ # 辅助数组，记录左(右)括号对应的右(左)括号位置
        aid = []
        for i in range(len_):
            if s[i] == '(':
                aid.append(i)
            elif s[i] == ')':
                leftid = aid.pop()
                cor[leftid] = i
                cor[i] = leftid
        
        string = ""
        step = 1 # 1往右，-1往左，该算法也叫往左往右
        index = 0 # 从第一个开始
        while(index<len_):
            if s[index] == '(' or s[index] == ')': # 遇到就跳一次，到对应的左or右括号
                index = cor[index]
                step = -step # 方向反转
            else:
                string += s[index]
            index += step
        return string