###############################################################################################
# 在题目规定的唯一元素的条件下，还是很简单的
###########
# 时间复杂度：O(n)
# 空间复杂度：O(n)
###############################################################################################
class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        dict_ = defaultdict(list)
        for pair in adjacentPairs:
            dict_[pair[0]].append(pair[1])
            dict_[pair[1]].append(pair[0])
        
        res = []
        for per in dict_:
            if len(dict_[per]) == 1:
                res.append(per)
                res.append(dict_[per][0])
                break
        
        for _ in range(len(adjacentPairs) - 1): # 题目保证元素唯一
            res.append(dict_[res[-1]][0] if res[-2] != dict_[res[-1]][0] else dict_[res[-1]][1])
        return res