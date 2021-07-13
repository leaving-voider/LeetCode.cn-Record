###############################################################################################
# 此题较难，对扫描线方法还不是很熟悉
###########
# 时间复杂度：O(nlogn + n^2)，排序 + 遍历O(n)以及每次遍历中max的O(n)
# 空间复杂度：O(n)
###############################################################################################
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        lines = []
        for l, r, h in buildings:
            lines.append([l, -h]) # 负高表示左
            lines.append([r, h])
        
        lines.sort(key = lambda x:(x[0], x[1])) # 当x同，左边排在右边前面

        heights = [0]
        res = []
        pre_point_h = cur_point_h = 0 # 分别表示前一个和当前关键点的高度
        for x, h in lines:
            if h < 0:
                heights.append(-h)
            else:
                heights.remove(h) # 一次只会remove一个
            cur_point_h = max(heights) # 不断寻找新的关键点
            if cur_point_h != pre_point_h:
                res.append([x, cur_point_h])
                pre_point_h = cur_point_h
        return res