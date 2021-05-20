###############################################################################################
# 主要是哈希+排序
###########
# 时间复杂度：O(l×n+l×mlogm)，构造哈希表时耗时l*n，分别是字符串平均长度和字符串个数，插入时需要遍历每一个字符串，且要通过比较看是否已在哈希表内
# m 表示实际字符串种类数，l×mlogm 的时间完成最坏情况（所有字符串出现频率相同）字符串比较，mlogm为sorted函数排序，l为比较时间
# 空间复杂度：O(l×m)，哈希表和排序所需空间均为此大小
###############################################################################################
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        statistics = Counter(words)
        list_ = sorted([[per, statistics[per]] for per in statistics], key=lambda k: (-k[1], k[0]))
        return [per[0] for per in list_[:k]]