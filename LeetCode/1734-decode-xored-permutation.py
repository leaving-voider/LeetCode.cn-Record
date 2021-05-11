###############################################################################################
# 纯数学解法，先求得perm[0]，其他迎刃而解
###########
# 时间复杂度：O(n)，n为perm数组长度
# 空间复杂度：O(1)，空间复杂度不考虑返回值，因此为常数复杂度
###############################################################################################
class Solution:
    def decode(self, encoded: List[int]) -> List[int]:
        len_ = len(encoded)
        o1 = 0
        for i in range(1, len_+2):
            o1 ^= i
        for i in range(1, len_, 2):
            o1 ^= encoded[i]
        
        o = [o1]
        for i in range(0, len_):
            o.append(o[-1]^encoded[i])
        return o