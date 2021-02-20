###############################################################################################
# 由于我是采用硬破解法，直接导致超出时间限制，因此学习官方给的参考答案
# 本质有两个滑动窗口，第一个滑动窗口为极大的包含K个不同整数的区间，第二个为极大包含K-1个的区间
###########
# 时间复杂度：O(n)，其中 n 是数组长度，至多只需要遍历该数组三次（右指针和两个左指针各一次）
# 空间复杂度：O(n)，其中 n 是数组长度。我们需要记录每一个数的出现次数，本题中数的大小不超过数组长度。
###############################################################################################
import collections
class Solution:
    def subarraysWithKDistinct(self, A, K) -> int:
        num1, num2 = collections.Counter(), collections.Counter() # 引用collections的计数器，分别记K极大滑动窗口和K-1极大滑动窗口内的每个数的个数
        tot1 = tot2 = 0 # 分别记K极大滑动窗口和K-1极大滑动窗口内的不同数的个数
        left1 = left2 = right = 0 # 两个左指针，一个右指针，实现滑动窗口
        ret = 0 # 记录满足条件的子集总数

        # 遍历每个数，并以其为右指针处
        for right, num in enumerate(A):
            # K极大
            if num1[num] == 0:
                tot1 += 1 # 不同数+1
            num1[num] += 1
            # K-1极大
            if num2[num] == 0:
                tot2 += 1
            num2[num] += 1
            
            # K极大
            while tot1 > K:
                # 减去最左边的数
                num1[A[left1]] -= 1
                # 若减去就没了，则不同数个数也-1
                if num1[A[left1]] == 0:
                    tot1 -= 1
                # 左指针右移
                left1 += 1
            # K-1极大
            while tot2 > K - 1:
                # 也减去小滑动窗口的最左的数
                num2[A[left2]] -= 1
                if num2[A[left2]] == 0:
                    tot2 -= 1
                left2 += 1
            
            # 一旦以上两个while的条件满足了，两个区间无交集处就是满足条件的子集，直接减去就能得到数量
            ret += left2 - left1
        
        return ret