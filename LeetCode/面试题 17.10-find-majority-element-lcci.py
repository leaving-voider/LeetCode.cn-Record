###############################################################################################
# 虽然时间快，但用了额外空间，不满足题目要求
###########
# 时间复杂度：O(n)
# 空间复杂度：O(n)
###############################################################################################
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        x = defaultdict(int)
        for per in nums:
            x[per] += 1
        max_, res = len(nums)//2, -1
        for per in x:
            if x[per] > max_:
                max_ = x[per]
                res = per
        return res


###############################################################################################
# Boyer-Moore投票算法
###########
# 时间复杂度：O(n)
# 空间复杂度：O(1)，只需要常数的额外空间
###############################################################################################
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Boyer-Moore 投票算法, 两次遍历
        candidate = nums[0]
        count = 1
        # 一次遍历，最后出来的candidate不一定是数量最多的那个数，但如果有哪个数的个数过半，那一定是它
        for i in range(1, len(nums)):
            if nums[i] == candidate: # 相同，则数量+=1
                count += 1
            else: # 不同
                count -= 1 # 先-=1
                if count < 0: # 如果小于0，说明在和这个nums[i]抵消前已经是0了，那么candidate换人
                    candidate = nums[i]
                    count = 1
        # 二次遍历，检查最后这个candidate是否是主要元素
        num = 0
        for per in nums:
            if per == candidate:
                num += 1
        return candidate if num > len(nums)/2 else -1