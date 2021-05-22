###############################################################################################
# 纯数学题，因为Alice先手，但凡开局数组有偶数个数，Alice必胜；若奇数个，Bob必胜
# 唯一一个特殊条件，即开局所有数不论奇偶，直接异或就是0，那直接判Alice胜
# 下面先判断偶数个，是因为免得每次调用都先计算所有的reduce了，能通过奇偶判断则不进行多的运算
###########
# 时间复杂度：O(n)，n 是数组 nums 的长度，最坏情况计算整个数组的XOR结果
# 空间复杂度：O(1)，无额外空间消耗，返回值xorsum不算
###############################################################################################
class Solution:
    def xorGame(self, nums: List[int]) -> bool:
        if len(nums) % 2 == 0:
            return True
        
        xorsum = reduce(xor, nums) # from functools import reduce; from operator import xor
        return xorsum == 0