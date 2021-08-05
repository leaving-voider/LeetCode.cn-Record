###############################################################################################
# 排序 + 哈希
###########
# 时间复杂度：O(n*mlogm)，n是字符串个数，m是字符串平均长度
# 空间复杂度：O(n*m)，如果字符串在哈希表里不是存储的本身，则只有O(n)
###############################################################################################
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for s in strs:
            dic[''.join(sorted(s))].append(s)
        
        return [dic[key] for key in dic]


###############################################################################################
# 使用每个字母的个数进行编码，使得异位词是同一类
###########
# 时间复杂度：O(n*(m + Σ))，n是字符串个数，m是字符串平均长度, Σ是字符集长度，这里是26，需要Σ的时间生成键
# 空间复杂度：O(n*Σ)，存的大小和字符集大小有关
###############################################################################################
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for s in strs:
            chs = [0]*26 # 存储每个字母的个数
            for ch in s:
                chs[ord(ch)-ord('a')] += 1
            dic[tuple(chs)].append(s)
        return [dic[key] for key in dic]