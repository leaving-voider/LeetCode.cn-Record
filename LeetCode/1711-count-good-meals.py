###############################################################################################
# 利用哈希表，降低时间复杂度
###########
# 时间复杂度：O(nlogC), 其中 n 是数组 deliciousness 的长度，C 是数组 deliciousness 中的元素值上限，这道题中 C=2^20
### 遍历deliciousness一次，每次遍历都需要logC的时间计算包含了该元素的大餐数量
# 空间复杂度：O(n), 哈希表空间消耗
###############################################################################################
class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        res, MOD = 0, 1000000007
        hash_ = defaultdict(int) # 存放美味为什么值的数量
        for per in deliciousness:
            for power_ in [1<<i for i in range(22)]:
                res = (res + hash_[power_ - per]) % MOD # 若存在某值+per == power_，则加上这个值的数量
            hash_[per] += 1
        return res