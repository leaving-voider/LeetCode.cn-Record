###############################################################################################
# 纯数学解法，先求得perm[0]，其他迎刃而解
###########
# 时间复杂度：O(n+m)，n和m分别是arr数组和queries数组的长度
# 空间复杂度：O(n)，flatMatrix空间消耗
###############################################################################################
class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        flatMatrix = [0]
        for per in arr:
            flatMatrix.append(flatMatrix[-1]^per)
        res = []
        for first, second in queries:
            res.append(flatMatrix[first]^flatMatrix[second+1])
        return res