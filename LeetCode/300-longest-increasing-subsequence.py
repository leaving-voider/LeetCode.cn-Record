###############################################################################################
# 官方方法1：动态规划，思路为以第i个数结尾的最长子串长度dp[i]为max(dp[j])+1，只要i>j且nums[i]>nums[j]
###########
# 时间复杂度：O(n²)，n 为数组 nums 的长度，更细来说是(1/2)*n²，十分耗时
# 空间复杂度：O(n)，dp数组
###############################################################################################
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        len_ = len(nums)
        if len_ == 0:
            return 0
        
        dp = [] # 以第i个为结尾的最长序列的动态规划
        for i in range(len_):
            dp.append(1) # 如果没有比前面任何一个子串大，则以该数结尾的长度只有1
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)


###############################################################################################
# 官方方法2：贪心+二分，维护一个数组dp，dp[0]=nums[0]，依次遍历nums中每个数，如果nums[i]大于dp[-1]
# 则加到dp最后，若小于，则在dp中使用二分查找一个合适的位置(dp[j-1]<nums[i]<dp[j])并替换掉dp[j]
# 这样最后len(dp)即我们要的最长子序列长度
###########
# 时间复杂度：O(n*logn)，n 为数组 nums 的长度，logn为二分查找
# 空间复杂度：O(n)，longest数组产生
###############################################################################################
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # 在nums找x合适插入替换的位置, 即nums[i-1] < x < nums[i], x替换nums[i]
        def bisect_(nums, x):
            l, r = 0, len(nums) - 1
            biggerThanX = r + 1 # 若递增序列没有比x大的，则返回最新的插入点的位置，即nums[-1]之后
            while(l<=r):
                mid = (l+r)//2
                if nums[mid] >= x:
                    r = mid - 1
                    biggerThanX = mid
                else:
                    l = mid + 1
            return biggerThanX
        
        longest = [nums[0]]
        for i in range(1, len(nums)):
            # ### 通用写法，可压缩代码行数，不过会增加查找次数
            # loc = bisect_(longest, nums[i])
            # # # 采用[loc:loc+1]方式就不会out of index，不过得数组[nums[i]]赋值数组才行
            # longest[loc:loc+1] = [nums[i]]

            ### 常规写法
            if nums[i] > longest[-1]:
                longest.append(nums[i])
            else:
                loc = bisect_(longest, nums[i])
                longest[loc] = nums[i]

        return len(longest)