###############################################################################################
# 自解
# 排序使用python中list类自带的reverse函数，会增加内存消耗，但运行更快
###############################################################################################
class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        xx = list(str(x))
        len_ = len(xx)
        big = 2**31
        max_ = big - 1
        min_ = -big
        xx.reverse()
        if xx[-1] == '-':
            xx.remove('-')
            xx = '-' + ''.join(xx).lstrip('0')
        else:
            xx = ''.join(xx).lstrip('0')

        int_ = int(xx)
        if int_ >= min_ and int_ <= max_:
            return int_
        return 0

###############################################################################################
# 自解
# 排序使用自己编写的for循环，内存消耗减少，但运行更慢
###############################################################################################
class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        xx = list(str(x))
        len_ = len(xx)
        big = 2**31
        max_ = big - 1
        min_ = -big
        if xx[0] == '-':
            for i in range(1, (len_-1)//2+1):
                xx[i], xx[len_-i] = xx[len_-i], xx[i]
            xx = ''.join(xx)
            xx = '-' + xx[1:].lstrip('0')
        else:
            for i in range(0, len_//2):
                xx[i], xx[len_-i-1] = xx[len_-i-1], xx[i]
            xx = ''.join(xx).lstrip('0')

        int_ = int(xx)
        if int_ >= min_ and int_ <= max_:
            return int_
        return 0