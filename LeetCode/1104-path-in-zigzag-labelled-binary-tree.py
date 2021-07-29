###############################################################################################
# 根据二叉树编号的性质就可解了
###########
# 时间复杂度：O(loglabel)
# 空间复杂度：O(1)
###############################################################################################
class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        i, level = label, 1
        while i != 1: # 先得到label在第几层
            level += 1
            i //= 2
        
        res, num = [], label
        while level > 0: # 往上走
            res.append(num)
            level -= 1
            min_ = 2**(level-1) # 该层最小值
            max_ = 2*min_ - 1 # 该层最大
            num = max_ + min_ - num//2 # 编号都得是上一层原本的编号num//2在该层的取反
        return res[::-1]