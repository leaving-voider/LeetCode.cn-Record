###############################################################################################
# 一次遍历自解通过。先排个序，然后从大到小遍历h的可能值，h最大也只可能为论文的个数，如果从len(citations)
# 到1都不是h的取值，那只能是0；之所以要从小到大，是因为原题告诉h有多值时，取最大
###########
# 时间复杂度：O(nlogn)，n 为 len(citations), 主要消耗为排序
# 空间复杂度：O(logn)，递归排序的空间复杂度
###############################################################################################
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        for i in range(len(citations), 0, -1):
            if citations[len(citations) - i] >= i:
                return i
        return 0