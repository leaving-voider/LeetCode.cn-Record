###############################################################################################
# 遍历一次 + 排序
###########
# 时间复杂度：O(n^2)
# 空间复杂度：O(n)
###############################################################################################
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        r, c = len(mat), len(mat[0])
        weakest = []
        for i in range(r):
            soldier_num = 0
            for j in range(c):
                if mat[i][j] == 1:
                    soldier_num += 1
            weakest.append((i, soldier_num))
        weakest.sort(key=lambda x:(x[1], x[0]))
        return [per[0] for per in weakest[:k]]