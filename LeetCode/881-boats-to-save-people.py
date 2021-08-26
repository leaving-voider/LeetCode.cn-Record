###############################################################################################
# 基于一点贪心思想 + 哈希，但还是有点暴力的感觉
###########
# 时间复杂度：O(n^2), 这个n受限于limit的值
# 空间复杂度：O(n)，这个n受限于people的个数
###############################################################################################
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        weights = defaultdict(int)
        for weight in people:
            weights[weight] += 1
        res = 0
        for weight in people:
            if weights[weight]:
                weights[weight] -= 1 # 免得把自己当作配对了
                if weight < limit:
                    for per in range(limit-weight, 0, -1):
                        if weights[per] > 0:
                            weights[per] -= 1
                            break
                res += 1
        return res

###############################################################################################
# 这个的贪心不是上面所用的：非要两个最接近limit进行组合，而是另一种贪心思想
# 而是看每个最小的，如果最大的和自己不能组合，那这个最大的和谁都不能组合，只有单独一个船
# 如果当前最小的和最大的可以组合，那这个最小的可以和任何一个人组合，但还是和最大的进行组合，充分利用船的容量
###########
# 时间复杂度：O(nlogn), 主要消耗是排序
# 空间复杂度：O(logn)，排序的栈消耗
###############################################################################################
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        res, n = 0, len(people)
        i, j = 0, n-1
        while i <= j:
            if people[i] + people[j] <= limit:
                i += 1 # 只有当最小的这个可以和最大的配对，i才右移
            j -= 1
            res += 1
        return res