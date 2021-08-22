###############################################################################################
# 稍加分析，便知只需要计算谁现到target点，谁就立于不败之地，所以直接计算到target距离即可，如果每个ghost
# 离target的距离都严格大于我（0，0）离target的距离，那么我肯定赢，否则，我一定输
###########
# 时间复杂度：O(n), n是ghosts的个数
# 空间复杂度：O(1)
###############################################################################################
class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        dis = abs(target[0]) + abs(target[1])
        for x, y in ghosts:
            if abs(x-target[0]) + abs(y-target[1]) <= dis:
                return False
        return True