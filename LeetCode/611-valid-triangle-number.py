###############################################################################################
# 思路简单，O(n^2logn)的算法，刚好卡到时间过
# 先排序，然后n^2遍历每个两两组合，但 0 < j < i
# 然后每次二分第一个 k，使得nums[k] > nums[i] - nums[j]，因此j-r就是满足三角不等式的
# 注意的是还需要去掉所有0
###########
# 时间复杂度：O((n^2)*logn)
# 空间复杂度：O(logn), 排序消耗
###############################################################################################
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        while nums and not nums[0]:
            nums.pop(0)
        res, len_ = 0, len(nums)
        for i in range(len_-1, 1, -1):
            for j in range(1, i):
                diff = nums[i] - nums[j]
                l, r = 0, j-1
                while l < r:
                    mid = (l+r)>>1
                    if nums[mid] > diff:
                        r = mid
                    else:
                        l = mid + 1
                res += j - r if nums[r] > diff else 0
        return res

# 一样排序 + 双指针，因为三指针不行，会漏掉一些，那双指针一定行，时间复杂度到了O(n^2)
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        res, len_ = 0, len(nums)
        for k in range(len_):
            i, j = k+1, k+2
            while j < len_:
                if nums[j] - nums[i] < nums[k]:
                    res += j - i
                    j += 1
                else:
                    if j - i > 1:
                        i += 1
                    else:
                        j += 1
        return res