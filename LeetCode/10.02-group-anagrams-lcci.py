###############################################################################################
# 直接暴力，遍历一次，每次要排序
###########
# 时间复杂度：O(n*klogk)，n为strs长度，k为每个串的长度
# 空间复杂度：O(nk)，哈希表存放全部字符串
###############################################################################################
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_ = defaultdict(list)

        for str_ in strs:
            dict_["".join(sorted(str_))].append(str_)
        
        return list(dict_.values())