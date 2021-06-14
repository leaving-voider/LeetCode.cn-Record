###############################################################################################
# 直接二分，答案在左闭右闭区间内
###########
# 时间复杂度：O(log(n))
# 空间复杂度：O(1)
###############################################################################################
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        a, b = 1, n
        while a < b:
            mid = (a+b)//2
            if guess(mid) == -1:
                b = mid - 1
            elif guess(mid) == 1:
                a = mid + 1
            else:
                return mid
        return a

## 也可以精简一点
class Solution:
    def guessNumber(self, n: int) -> int:
        a, b = 1, n
        while a < b:
            mid = (a+b)//2
            if guess(mid) <= 0:
                b = mid
            else:
                a = mid + 1
        return a