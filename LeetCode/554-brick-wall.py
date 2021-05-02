###############################################################################################
# 官方给的方法
# 主要解题思想在于如何判断两条边是否在同一条竖直直线上，能判断这个就能知道那条垂线能够经过最少砖块了
# 官方给的是将每行每块砖的右边与最左边之间的距离x计算出来进行判断，除了最右砖块的右边。
# 这样只要不同行的两个距离x1和x2相等，则这两个边属于同一竖直线
###########
# 时间复杂度：O(nm)，其中 n 是砖墙高度，m是砖平均数量
# 空间复杂度：O(nm)，官方给的哈希表，本python实现使用字典同样是哈希表，最坏情况下空间复杂度可能为O(nm)
###############################################################################################
class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        dict_ = {}
        height = len(wall)
        for i in range(height): # 纵向依次遍历
            sum_ = 0
            for j in range(len(wall[i])-1):
                sum_+=wall[i][j]
                if sum_ in dict_:
                    dict_[sum_] += 1
                else:
                    dict_[sum_] = 1
        if not bool(dict_):
            return height
        return height-max(dict_.values())