###############################################################################################
# 遍历一次
###########
# 时间复杂度：O(n)
# 空间复杂度：O(1)
###############################################################################################
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        i = 0
        k = 26**(len(columnTitle)-1)
        res = 0
        while i < len(columnTitle):
            res += (ord(columnTitle[i]) - ord('A') + 1)*k
            i += 1
            k //= 26
        return res