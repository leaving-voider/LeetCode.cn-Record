###############################################################################################
# 还是要利用基本的random库，自己实现不同数不同权重而已
###########
# 时间复杂度：O(n)
# 空间复杂度：O(n)
###############################################################################################
class Solution:

    def __init__(self, w: List[int]):
        self.pre = [0]
        for per in w:
            self.pre.append(per + self.pre[-1])
        self.total = sum(w)

    def pickIndex(self) -> int:
        pick = random.randint(1, self.total)
        l, r = 0, len(self.pre)-1
        while l < r:
            mid = (l+r+1)>>1
            if self.pre[mid] < pick:
                l = mid
            else:
                r = mid - 1
        return l