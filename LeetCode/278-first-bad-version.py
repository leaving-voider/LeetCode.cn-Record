###############################################################################################
# 直接二分，答案在左闭右闭区间内
###########
# 时间复杂度：O(log(n))，n是给定版本的数量
# 空间复杂度：O(1)
###############################################################################################
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        a, b = 1, n # 左闭右闭
        while a < b:
            mid = (a+b)//2
            if isBadVersion(mid):
                b = mid
            else:
                a = mid + 1
        return b # 返回哪个都一样