###############################################################################################
# 本题不难，之前做过类似的【前缀和+哈希】就能解决，但需要有注意的点
# 1、 0也算k的整数倍，因为0 = 0*k, 如同 k = 1*k
# 2、 若按一般的前缀和来做，判断两数之差为k的整数倍，要么用两个哈希表【index->sum和sum->index的映射】
# 要么只能遍历所有整数倍的值；但是官方直接使用一个性质来避免这个问题【若差为k的倍数，则两数取余的值相等】
###########
# 时间复杂度：O(n)，n 是数组 nums 的长度
# 空间复杂度：O(min(m,k))，主要消耗为哈希表，哈希表存储每个余数第一次出现的下标
###############################################################################################
class Solution:
    def checkSubarraySum(self, nums, k: int) -> bool:
        if len(nums) < 2:
            return False

        sum_, counter = 0, {0:-1} # 当从最左开始到某一个位置正好为k的整数倍时，需要counter中这个0

        for i, num in enumerate(nums):
            sum_ = (sum_+num)%k # 得到取余值即可，将判断两数相减的值为k的倍数 转化为 判断取余值相等 即可（免去遍历所有的倍数）
            if sum_ not in counter:
                counter[sum_] = i # 前缀和 对应的 index
            else: # 若有取余值相同的已经出现过，则判断一次 是否满足子数组长大于2
                prevIndex = counter[sum_]
                if i - prevIndex > 1: # 即便不满足，没关系，不需要用这次的取余值的index来替换，因为只需要最长的那个大于2就能直接返回True
                    return True
        return False

###############################################################################################
# 自己写的，超出时间限制，主要是遍历了所有的k的倍数
# 利用官方给的一个性质【若差为k的倍数，则两数取余的值相等】可解决这个问题
###############################################################################################
class Solution:
    def checkSubarraySum(self, nums, k: int) -> bool:
        len_ = len(nums)
        if len_ < 2:
            return False
        sum_ = 0
        counter = {0:-1} # 当从最左开始到某一个位置正好为k的整数倍时，需要这个0
        for i in range(len_):
            sum_ += nums[i]
            max_ = sum_ // k
            for j in range(max_+1):
                if (sum_ - j*k) in counter and i - counter[sum_ - j*k] > 1:
                    return True
            if sum_ not in counter: # 防止中间有0，把相同的sum_覆盖了
                counter[sum_] = i # 记录index
        return False