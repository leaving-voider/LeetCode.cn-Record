###############################################################################################
# 经典数位统计，就是麻烦，分类讨论
###########
# 时间复杂度：O(logn)，遍历每一位
# 空间复杂度：O(n)
###############################################################################################
class Solution:
    def countDigitOne(self, n: int) -> int:
        if not n:
            return 0
        len_, res = len(str(n)), 0
        num = []
        def get(num, l, r):
            res = 0
            for i in range(l, r-1, -1):
                res = res*10 + num[i]
            return res
        while n:
            num.append(n%10)
            n //= 10
        for i in range(len_-1, -1, -1):
            if i < len_-1:
                res += get(num, len_-1, i+1)*(10**i) # 高位更小时
            # 高位相同时
            if num[i] > 1:
                res += 10**i
            elif num[i] == 1:
                res += get(num, i-1, 0) + 1
        return res