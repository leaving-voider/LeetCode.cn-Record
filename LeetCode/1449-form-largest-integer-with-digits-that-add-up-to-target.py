###############################################################################################
# 此题有点难度，最大难度在于想到动规只能解决一半问题，先通过动规拿到最长位数，在通过另一个位置转换数组
# 来记录转移来源，得到最大的数
# 如下是半参考半自己写，得到的解法，不过超时了；但同时也因此题知道了一个很好的规律，即
# dp[i][j] = max([dp[i-1][j-per*cost_]+per for per in range(j//cost_+1)]) 和 dp[i][j] = max(dp[i-1][j], dp[i][j-cost_]+1) 是等价的
###########
# 时间复杂度：O(n*target*total)，total为组成的和/当前数的大小，n是cost数组大小，在此题中为9
# 空间复杂度：O(n*target)，动规数组开销
###############################################################################################
class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        # 定义dp[i][j]：任意使用前i个cost，得到和为j，所得到的整数的最长位数
        dp = [[0]*(target+1) for _ in range(10)]
        from_ = [[0]*(target+1) for _ in range(10)] # 不能写成dp = from_ = ... 会指向同一个内存
        for i in range(1, target+1):
            dp[0][i] = float("-inf") # 不可能的状态，设位数为很小
        for i in range(1, 10):
            cost_ = cost[i-1]
            for j in range(target+1):
                if j < cost_: # cost_无法使用
                    dp[i][j] = dp[i-1][j]
                    from_[i][j] = j
                else:
                    max_, max_k = dp[i-1][j], 0
                    for k in range(1, j//cost_+1):
                        if dp[i-1][j-k*cost_]+k >= max_: # 大于等于是为了尽量取更大的数
                            max_ = dp[i-1][j-k*cost_]+k
                            max_k = k
                    dp[i][j] = max_
                    # 其实这里的写法和写成dp[i][j] = max(dp[i-1][j], dp[i][j-cost_]+1)是等价的
                    # dp[i][j] = max([dp[i-1][j-per*cost_]+per for per in range(j//cost_+1)])
                    from_[i][j] = j - cost_ if max_k != 0 else j
        if dp[9][target]<0: # 没找到
            return "0"
        i, j, res = 9, target, ""
        while(i>0):
            if from_[i][j] == j: # 表示从上一层而来，第i个数没使用
                i -= 1
            else:
                res += str(i)
                j = from_[i][j]
        return res

## 利用找到的等价性，直接进行优化，减少一个循环
class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        # 定义dp[i][j]：任意使用前i个cost，得到和为j，所得到的整数的最长位数
        dp = [[0]*(target+1) for _ in range(10)]
        from_ = [[0]*(target+1) for _ in range(10)] # 不能写成dp = from_ = ... 会指向同一个内存
        for i in range(1, target+1):
            dp[0][i] = float("-inf") # 不可能的状态，设位数为很小
        for i in range(1, 10):
            cost_ = cost[i-1]
            for j in range(target+1):
                if j < cost_: # cost_无法使用
                    dp[i][j], from_[i][j] = dp[i-1][j], j
                else:
                    dp[i][j], from_[i][j] = (dp[i-1][j], j) if dp[i-1][j] > dp[i][j-cost_]+1 else (dp[i][j-cost_]+1, j - cost_)
        if dp[9][target]<0: # 没找到
            return "0"
        i, j, res = 9, target, ""
        while(i>0):
            if from_[i][j] == j: # 表示从上一层而来，第i个数没使用
                i -= 1
            else:
                res += str(i)
                j = from_[i][j]
        return res


## 本来按理论分析，可以避免单独在最后进行倒退找数字，但由于有字符串的操作和存储，如下代码虽然精简，但并没表现良好，时空消耗均增大
class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        # 定义dp[i][j]：任意使用前i个cost，得到和为j，所得到的整数的最长位数
        dp = [[0]*(target+1) for _ in range(10)]
        string = [[""]*(target+1) for _ in range(10)]
        for i in range(1, target+1):
            dp[0][i] = float("-inf") # 不可能的状态，设位数为很小
        for i in range(1, 10):
            cost_ = cost[i-1]
            for j in range(target+1):
                if j < cost_: # cost_无法使用
                    dp[i][j], string[i][j] = dp[i-1][j], string[i-1][j]
                else:
                    dp[i][j], string[i][j] = (dp[i-1][j], string[i-1][j]) if dp[i-1][j] > dp[i][j-cost_]+1 else (dp[i][j-cost_]+1, string[i][j-cost_] + str(i))
        if dp[9][target]<0: # 没找到
            return "0"
        return string[9][target][::-1]


## 按上面基于string数组的存储进行优化：优化dp和string空间，优化第二层循环的范围
## 至此，代码已经非常精简，但由于有字符串的操作，时间空间消耗都挺大
class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        # 定义dp[i][j]：任意使用前i个cost，得到和为j，所得到的整数的最长位数
        dp = [float("-inf")]*(target+1) # 从第0层开始初始化
        dp[0], string = 0, [""]*(target+1) 
        for i, cost_ in enumerate(cost):
            for j in range(cost_, target+1):
                if dp[j] <= dp[j-cost_]+1:
                    dp[j], string[j] = dp[j-cost_]+1, string[j-cost_] + str(i+1)
        return "0" if dp[target]<0 else string[target][::-1]


###############################################################################################
# 放弃使用string的方式来使代码简洁，为了提高运行效率，因此基于原来的倒退找数来进行优化
# 看了下官方的from数组优化，直接整个去掉了，比我用string数组来代替还厉害；不过from数组确实没法改成一维
# 从本质上（定义上）来看，from变成一维不能得到完整的回退信息，但dp即便只有最后一层也可以，因为按照定义
# 最后一层dp[j]表示在前9个数中，得到和为j，所用到的整数的最长位数，此时如果对于从大到小的某个cost有
# dp[j] == dp[j - cost] + 1，则说明对于这个cost的数是被使用了的（之所以能这样，不需要更早一层的dp，
# 是因为当dp[j] ！= dp[j - cost] + 1的时候，一定有dp[j] = dp[j]，即就是上一层的值！）
###########
# 时间复杂度：O(n*target)，其中 n 是数组 cost 的长度
# 空间复杂度：O(target)
###############################################################################################
class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        # 定义dp[i][j]：任意使用前i个cost，得到和为j，所得到的整数的最长位数
        dp = [float("-inf")]*(target+1) # 不可能的状态，设位数为很小
        dp[0] = 0 # 从i=0开始初始化，dp[0]表示组成0的时候位数也为0
        for cost_ in cost:
            for j in range(cost_, target+1):
                dp[j] = max(dp[j],dp[j-cost_]+1)
        if dp[target]<0: # 没找到
            return "0"
        total, res = target, ""
        for i in range(8, -1, -1):
            c = cost[i]
            while total >= c and dp[total] == dp[total - c] + 1:
                res += str(i + 1)
                total -= c
        return res