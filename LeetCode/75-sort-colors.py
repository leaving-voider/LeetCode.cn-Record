###############################################################################################
# 题目要求modify in-place，快排就是in-place,只不过复杂度高于O(n)
###########
# 时间复杂度：O(nlogn)
# 空间复杂度：O(logn)
###############################################################################################
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        def quick_sort(nums, l, r):
            if l >= r:
                return
            pick, i, j = nums[(l+r)>>1], l-1, r+1
            while i < j:
                i += 1
                while nums[i] <  pick:
                    i += 1
                j -= 1
                while nums[j] > pick:
                    j -= 1
                if i < j:
                    nums[i], nums[j] = nums[j], nums[i]
            quick_sort(nums, l, j)
            quick_sort(nums, j+1, r)
        quick_sort(nums, 0, len(nums)-1)

###############################################################################################
# 单指针 + 两次遍历
###########
# 时间复杂度：O(n)
# 空间复杂度：O(1)
###############################################################################################
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        head = 0
        for i in range(len(nums)): # 第一次遍历，把所有0放到列表前面
            if nums[i] == 0:
                nums[head], nums[i] = nums[i], nums[head]
                head += 1
        for i in range(head, len(nums)): # 第二次遍历，把所有1都放到前面
            if nums[i] == 1:
                nums[head], nums[i] = nums[i], nums[head]
                head += 1

###############################################################################################
# 双指针 + 1次遍历（换0和1）
###########
# 时间复杂度：O(n)
# 空间复杂度：O(1)
###############################################################################################
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        p0 = p1 = 0 # p0换0，p1换1
        for i in range(len(nums)): # 第一次遍历，把所有0放到列表前面
            if nums[i] == 1:
                nums[p1], nums[i] = nums[i], nums[p1]
                p1 += 1
            elif nums[i] == 0:
                nums[p0], nums[i] = nums[i], nums[p0]
                if p1 > p0: # 说明把1换出去了一个
                    nums[p1], nums[i] = nums[i], nums[p1]
                p1 += 1 # 不管1有没有换出去，p1都要+1，不然又会把0换出去，所以我们要保持p1>=p0
                p0 += 1

###############################################################################################
# 双指针 + 1次遍历（换0和2），这种有点类似于用了一次pick=1的quick_sort
###########
# 时间复杂度：O(n)
# 空间复杂度：O(1)
###############################################################################################
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        p0, p2 = 0, len(nums)-1
        for i in range(len(nums)): # 第一次遍历，把所有0放到列表前面
            while p2 >= i and nums[i] == 2: # p2也不能减过度了，把前面排好的都换了
                nums[p2], nums[i] = nums[i], nums[p2]
                p2 -= 1
            if nums[i] == 0: # 这个本来就是0 or p2换过来的0
                nums[p0], nums[i] = nums[i], nums[p0]
                p0 += 1