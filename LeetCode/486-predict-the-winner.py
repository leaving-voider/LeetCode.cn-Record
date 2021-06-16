##################################################
# 整个题的递归和动规的思路都是从树的底层往上推
##################################################

###############################################################################################
# 递归解决，但不可避免地有大量的重复计算
###########
# 时间复杂度：O(2^n)，n为数组nums长
# 空间复杂度：O(n)，递归消耗栈空间
###############################################################################################
class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        def total(start: int, end: int, turn: int) -> int:
            if start == end:
                return nums[start] * turn
            scoreStart = nums[start] * turn + total(start + 1, end, -turn)
            scoreEnd = nums[end] * turn + total(start, end - 1, -turn)
            # 这一步写法是为了保证玩家选了对自己最有利的那个，在玩家1时，需要返回总分最大那个；玩家2出手时，返回总分小那个
            return max(scoreStart * turn, scoreEnd * turn) * turn
        
        return total(0, len(nums) - 1, 1) >= 0

## 换一种写法，去掉turn变量
class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        def total(start: int, end: int) -> int:
            if start == end:
                return nums[start]
            scoreStart = nums[start] - total(start + 1, end)
            scoreEnd = nums[end] - total(start, end - 1)
            # 两个玩家，在每一步都考虑使得自己的得分最高
            return max(scoreStart, scoreEnd)
        return total(0, len(nums) - 1) >= 0

###############################################################################################
# 按照上面第二种写法，很明显，可以把递归换成动规，用空间换时间，减少重复计算
# 如果要理解该动规dp[i][j]的含义：表示在[i, j]的左闭右闭区间，玩家能获得的最大利益
# 默认为玩家1先手，所以最后返回的dp[0][len_-1]的范围只能是玩家1的最大利益，若＞0则玩家1赢，小于0则玩家2赢
###########
# 时间复杂度：O(n^2)，n为数组nums长，计算数组中的状态
# 空间复杂度：O(n^2)，动规数组消耗
###############################################################################################
class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        len_ = len(nums)
        dp = [[0]*len_ for _ in range(len_)]
        for i in range(len_):
            dp[i][i] = nums[i]
        for i in range(len_-1, -1, -1):
            for j in range(i+1, len_):
                dp[i][j] = max(nums[i]-dp[i+1][j], nums[j]-dp[i][j-1])
        return dp[0][len_-1] >= 0

## 减少一个遍历
class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        len_ = len(nums)
        dp = [[0]*len_ for _ in range(len_)]
        for i in range(len_-1, -1, -1):
            dp[i][i] = nums[i]
            for j in range(i+1, len_):
                dp[i][j] = max(nums[i]-dp[i+1][j], nums[j]-dp[i][j-1])
        return dp[0][len_-1] >= 0


###############################################################################################
# 同样，继续优化空间
###########
# 时间复杂度：O(n^2)，n为数组nums长，计算数组中的状态
# 空间复杂度：O(n)
###############################################################################################
class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        len_ = len(nums)
        dp = [0]*len_
        for i in range(len_-1, -1, -1):
            dp[i] = nums[i]
            for j in range(i+1, len_):
                dp[j] = max(nums[i]-dp[j], nums[j]-dp[j-1])
        return dp[len_-1] >= 0
