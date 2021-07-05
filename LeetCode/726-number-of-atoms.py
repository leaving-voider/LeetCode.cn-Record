###############################################################################################
# 参考了下官方，栈 + 哈希，思路不难，只是在实现的时候是往栈里存放哈希字典，且栈用list替代
###########
# 时间复杂度：O(n^2), n为formula的长度，最坏情况栈有n/2层，按n算，每层出来要更新一遍上一层的原子数量，也算O(n)
### 遍历结束后，排序耗时 O(nlogn)，因此O(n^2 + nlogn) = O(n^2)
# 空间复杂度：O(n), 栈中哈希表的元素个数，不会超过n
###############################################################################################
class Solution:
    def countOfAtoms(self, formula: str) -> str:
        stack = []
        stack.append(defaultdict(int))
        i = 0
        len_ = len(formula)
        while i < len_:
            ch = formula[i]
            if ch == '(':
                stack.append(defaultdict(int))
            elif ch == ')':
                num = 0
                while i+1 < len_ and formula[i+1].isdigit():
                    num = num*10 + int(formula[i+1])
                    i += 1
                num = 1 if num == 0 else num
                d = stack.pop()
                for per in d:
                    d[per] *= num
                    stack[-1][per] += d[per]
            else:
                while i+1 < len_ and formula[i+1].islower():
                    ch += formula[i+1]
                    i += 1
                num = 0
                while i+1 < len_ and formula[i+1].isdigit():
                    num = num*10 + int(formula[i+1])
                    i += 1
                num = 1 if num == 0 else num
                stack[-1][ch] += num
            i += 1
        list_ = list(stack[-1])
        list_.sort()
        res = ""
        for per in list_:
            res += per
            if stack[-1][per] > 1:
                res += str(stack[-1][per])
        return res