###############################################################################################
# 题目稍微有点难理解，看明白后难度不大，只需要分别对不同queries进行处理即可
# 利用前缀和，将不同类别的糖果数总和，便于使用
###########
# 时间复杂度：O(n+q)，n 和 q 分别是数组 candiesCount 和 queries 的长度，O(n) 的时间计算前缀和
# 空间复杂度：O(n)，存储前缀和数组需要的空间，返回值不计入空间复杂度
###############################################################################################
class Solution:
    def canEat(self, candiesCount: List[int], queries: List[List[int]]) -> List[bool]:
        # 提前处理candiesCount，求其前i类糖果总数
        totalCandies = [0]
        for candyNum in candiesCount:
            totalCandies.append(candyNum+totalCandies[-1])
        totalCandies.pop(0)
        answer = []
        # 循环，分别处理每个不相干的query
        for favoriteType, favoriteDay, dailyCap in queries:
            eatMin = favoriteDay + 1 # 每天吃1个
            eatMax = (favoriteDay + 1) * dailyCap # 每天吃最大个数
            eatTypeMin = totalCandies[favoriteType-1] + 1 if favoriteType != 0 else 1 # 该类糖果第一个
            eatTypeMax = totalCandies[favoriteType] # 该类糖果最后一个
            # 只要其中一个该类糖果在eatMin和eatMax之间即可
            answer.append(eatTypeMin <= eatMax and eatTypeMax >= eatMin) # 有交集判定

        return answer