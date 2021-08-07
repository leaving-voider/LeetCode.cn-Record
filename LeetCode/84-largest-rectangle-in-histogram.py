###############################################################################################
# 区间DP超时
###########
# 时间复杂度：O(n^2)
# 空间复杂度：O(n^2)
###############################################################################################
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        N = len(heights)
        dp = [[0]*N for _ in range(N)] # dp[i][j]: i到j之间的最大面积
        res = 0
        for i in range(N):
            dp[i][i] = heights[i] # 只有自己，就是自己的高度
            res = max(res, dp[i][i])
            if i < N-1:
                dp[i][i+1] = min(heights[i], heights[i+1])*2
                res = max(res, dp[i][i+1])
        
        for le in range(3, N+1):
            for i in range(N - le + 1):
                l, r = i, i+le-1 # 左闭右闭
                dp[l][r] = min(dp[l+1][r-1] // (r-l-1), heights[l], heights[r])*(r-l+1)
                res = max(res, dp[l][r])
        return res

###############################################################################################
# 单调栈，预处理每个位置i的左右两边离其最近且高度小于height[i]的，然后遍历每个高度即可
###########
# 时间复杂度：O(n)，单调栈预处理时，每个位置的数最多入栈一次出栈一次，因此也是O(n)的复杂度
# 空间复杂度：O(n)
###############################################################################################
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        N, res = len(heights), 0
        left, right = [0]*N, [0]*N # 预处理每个位置i左边和右边最近的且高度小于height[i]的位置
        mono_stack = []
        for i in range(N):
            while mono_stack and heights[i] <= heights[mono_stack[-1]]:
                mono_stack.pop()
            left[i] = mono_stack[-1] if mono_stack else -1 # -1 表示左边所有都比i的高度高
            mono_stack.append(i)
        mono_stack = []
        for i in range(N-1, -1, -1):
            while mono_stack and heights[i] <= heights[mono_stack[-1]]:
                mono_stack.pop()
            right[i] = mono_stack[-1] if mono_stack else N # N 表示右边所有都比i的高度高
            mono_stack.append(i)
        for i in range(N):
            l, r = left[i]+1, right[i]-1
            res = max(res, heights[i]*(r-l+1))
        return res

# 可以合并一下，这样还是能求出正确的左右边界
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        N, res = len(heights), 0
        left, right = [0]*N, [0]*N # 预处理每个位置i左边和右边最近的且高度小于height[i]的位置
        mono_stack1, mono_stack2 = [], []
        for i in range(N):
            while mono_stack1 and heights[i] <= heights[mono_stack1[-1]]:
                mono_stack1.pop()
            while mono_stack2 and heights[N-i-1] <= heights[mono_stack2[-1]]:
                mono_stack2.pop()
            left[i] = mono_stack1[-1] if mono_stack1 else -1 # -1 表示左边所有都比i的高度高
            mono_stack1.append(i)
            right[N-i-1] = mono_stack2[-1] if mono_stack2 else N # N 表示右边所有都比i的高度高
            mono_stack2.append(N-i-1)
        for i in range(N):
            l, r = left[i]+1, right[i]-1
            res = max(res, heights[i]*(r-l+1))
        return res

# 现在来一个不能求出正确右边界却不影响答案的，原因是只漏了一种情况，即右边有一堆和i高度一样的(假设为j~k)，这种情况我们只能找到最左的那个
# 但是这不影响答案，因为在我们遍历到j~k时，通过正确的左边界我们还是会进行一次最大面积的求解，所以不影响最终答案
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        N, res = len(heights), 0
        left, right = [0]*N, [N]*N # stack在循环结束后，还会剩一些没弹出来，这些没弹出来的就是右边没有比其小的，所以我们直接初始化为N即可
        mono_stack = []
        for i in range(N):
            while mono_stack and heights[i] <= heights[mono_stack[-1]]:
                t = mono_stack.pop()
                right[t] = i # 出栈的时候，说明遇到了右边第一个小于等于自己的（当然右边可能还有更多等于自己的，但没关系）
            left[i] = mono_stack[-1] if mono_stack else -1
            mono_stack.append(i)
        for i in range(N):
            l, r = left[i]+1, right[i]-1
            res = max(res, heights[i]*(r-l+1))
        return res


###############################################################################################
# 借鉴别人的分治思想，原本超时，但加了剪枝能过
###########
# 时间复杂度：O(nlogn)，每次递归都要找当前区间最小的数，递归一共logn层，每层都是n，因此O(nlogn)
# 空间复杂度：O(logn)，栈消耗
###############################################################################################
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        N, res = len(heights), 0
        
        def dfs(l, r):
            nonlocal res
            if l >= r:
                if l == r:
                    res = max(res, heights[l])
                return 
            
            min_ = float("inf")
            idx = -1
            last = heights[l] # 和第一个比就行了
            flag = 1 # 记录这个区间是不是都是一样的数
            for i in range(l, r+1):
                if heights[i] < min_:
                    min_ = heights[i]
                    idx = i
                if heights[i] != last:
                    flag = 0
            res = max(res, min_*(r-l+1))
            if flag: # 说明这个区间的数都一样
                return
            dfs(l, idx-1)
            dfs(idx+1, r)
        dfs(0, N-1)
        return res