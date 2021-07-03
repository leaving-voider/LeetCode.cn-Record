###############################################################################################
# 哈希+对defaultdict排序
###########
# 时间复杂度：O(n + klogk), k 是字符串 s 包含的不同字符的个数, 遍历字符串 + 排序需要 O(klogk) 的时间
# 空间复杂度：O(n*coins)
###############################################################################################
class Solution:
    def frequencySort(self, s: str) -> str:
        dict_ = defaultdict(int)
        for letter in s:
            dict_[letter] += 1
        res = ""
        for per in sorted(dict_, key=lambda x: -dict_[x]):
            res += per*dict_[per]
        return res