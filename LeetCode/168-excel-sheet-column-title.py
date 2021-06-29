###############################################################################################
# 按位转化成26进制
###########
# 时间复杂度：O(log_26_columnNumber), 时间复杂度即为将 columnNumber 转换成 26 进制的位数
# 空间复杂度：O(log_26_columnNumber), res的开销
###############################################################################################
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = []
        while columnNumber:
            # 先减1变成0-25的26进制，再加回来
            thisBit = (columnNumber - 1) % 26 + 1
            res.append(chr(thisBit + 64)) # 转化成对应的字母
            # 减去这个thisBit就是为了不会凭空多出一位，因为整个columnNumber都是从1开始的数，并不是标准的26进制
            # 所以这个thisBit改成1也是一样的 columnNumber = (columnNumber - 1) // 26
            columnNumber = (columnNumber - thisBit) // 26
        
        return "".join(res[::-1])

# 基于以上注释中的分析，可以把thisBit改成1，因此可以简写如下
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = []
        while columnNumber:
            # 这种可以理解成，每一位都-1，相当于 0 对应 A， 25 对应 Z
            columnNumber -= 1
            res.append(chr(columnNumber % 26 + 65)) # 转化成对应的字母
            columnNumber //= 26

        return "".join(res[::-1])