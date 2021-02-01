##############################################################
# 其实这道题我一开始是用两个循环遍历，但直接导致了超时，于是修改策略
# 从1开始去试，就免去了遍历，不过时间开销还是很庞大
# 官方给的答案思路和我一样，不过用了新的数据结构：哈希表
# python的set集合背后就是哈希表，帮助快速查找
##############################################################
class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        sum_a = sum(A)
        sum_b = sum(B)
        diff = (sum_a - sum_b)//2

        hash_a = set(A)
        for per in B:
            a = per+diff
            if a in hash_a:
                return [a, per]
        return [-1, -1]

# #################################################################
# # 我的方法，因为交换的量是已知的，两个人总量的差值除以2就是要交换的量X
# # 谁更多，谁给对方的糖的量就要比对方给自己的大X，然后从1开始一个一个试
# #################################################################
# class Solution:
#     def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
#         sum_a = sum(A)
#         sum_b = sum(B)
#         diff = abs(sum_a - sum_b)//2

#         for i in range(1, 100000):
#             if sum_a > sum_b:
#                 if i in B and (i+diff) in A:
#                     return [i+diff, i]
#             else:
#                 if i in A and (i+diff) in B:
#                     return [i, i+diff]
#         return [-1, -1]