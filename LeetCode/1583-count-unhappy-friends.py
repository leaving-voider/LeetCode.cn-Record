###############################################################################################
# 简单问题，看起来有三个循环，但实际复杂度没那么高
###########
# 时间复杂度：O(n^3)，最坏是O(n^3)，但实际没有，当然也可以像官方那样记录下标，减少一个循环
# 空间复杂度：O(n)
###############################################################################################
class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        mapping = defaultdict(int)
        for x, y in pairs:
            mapping[x], mapping[y] = y, x
        
        def is_happy(x):
            for pre in preferences[x]:
                if pre == mapping[x]:
                    break
                for other in preferences[pre]:
                    if other == mapping[pre]:
                        break
                    if other == x:
                        return False
            return True

        res = 0
        for per in mapping:
            if not is_happy(per):
                res += 1
        return res