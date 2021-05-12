###############################################################################################
# 利用异或性质，以空间复杂度为代价减少时间复杂度
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
