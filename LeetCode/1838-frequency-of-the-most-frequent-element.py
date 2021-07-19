###############################################################################################
# 自己写的暴力，超时了
###########
# 时间复杂度：O(n^2)
# 空间复杂度：O(n)
###############################################################################################
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        dict_ = defaultdict(int)
        for num in nums:
            dict_[num] += 1
        
        max_ = max(dict_.values())
        for per in dict_:
            t, cur = k, dict_[per]
            for i in range(1, k+1):
                if per - i in dict_:
                    cur += dict_[per - i] if dict_[per - i]*i < t else t//i
                    t -= dict_[per - i]*i
                if t <= 0:
                    break
            max_ = max(cur, max_)
        return max_


###############################################################################################
# 官方的 排序 + 滑动窗口，一次遍历
###########
# 时间复杂度：O(n*logn)，n为strs长度，k为每个串的长度
# 空间复杂度：O(logn)，递归排序消耗的栈空间
###############################################################################################
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        max_ = 1
        total = l = 0 # total表示把所有[l, r]间的数变成r需要加多少个1
        for r in range(1, len(nums)):
            total += (nums[r] - nums[r-1]) * (r - l)
            while total > k:
                total -= nums[r] - nums[l]
                l += 1
            max_ = max(max_, r - l + 1)
        return max_