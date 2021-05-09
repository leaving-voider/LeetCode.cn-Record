###############################################################################################
# 典型的二分查找题型，唯一要做的就是考虑如何判断长度为k的不重合的连续子序列的数量，即在某个DayLimit下
# 依次遍历即可，满足一个子序列则计数归0，若遇到此时没开花的，计数也归0
###########
# 时间复杂度：O(log(high-low)×n)，high是二分上限，即最大天数，low是最小开花天数，log(high-low)代表二分查找时间复杂度
# n代表每次遍历整个bloomDay的时间复杂度
# 空间复杂度：O(1)
###############################################################################################
class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def thisDayLimitIsOk(dayLimit):
            bouquetsNum = flowersSeqNum = 0 # 存放目前能制作的花束数量和当前花序列的长度

            for i in range(len(bloomDay)):
                if bloomDay[i] <= dayLimit:
                    flowersSeqNum += 1
                    if flowersSeqNum == k: # 此时可以制作一个花束
                        flowersSeqNum = 0 # 归0，因为花不能重复使用
                        bouquetsNum += 1
                        if bouquetsNum == m: # 如果已经能制作m数量的花束了，则直接返回True
                            return True
                else:
                    flowersSeqNum = 0 # 连续被打断，序列数归0
            return bouquetsNum == m

        if len(bloomDay) < m*k: # 花不够
            return -1
        
        low, high = min(bloomDay), max(bloomDay)
        while(low<high): # 默认左闭右开的写法
            mid = (low+high)//2
            if thisDayLimitIsOk(mid):
                high = mid # 默认左闭右开的写法
            else:
                low = mid + 1
        ## while循环判断也可改成如下
        # while(low<=high): # 默认左闭右闭的写法
        #     mid = (low+high)//2
        #     if thisDayLimitIsOk(mid):
        #         high = mid - 1 # 默认左闭右闭的写法
        #     else:
        #         low = mid + 1
        return low
