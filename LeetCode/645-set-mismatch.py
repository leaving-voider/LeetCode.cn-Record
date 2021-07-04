###############################################################################################
# 自己写的一次遍历的方法
###########
# 时间复杂度：O(n + 删除耗时), 遍历一次，每次还要删除
# 空间复杂度：O(n)
###############################################################################################
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        dict_ = {}
        res = [0, 0]
        list_ = [per for per in range(1,len(nums)+1)]
        for num in nums:
            try:
                list_.remove(num)
            except:
                res[1] = list_[0] # 这一句没用，只是为了保证语法完整性
            if num not in dict_:
                dict_[num] = 1
            else:
                res[0] = num
        res[1] = list_[0]
        return res

# 同样一次遍历，但省了每次的删除操作，最后利用python集合的+ - 法来得到元素，时间复杂度大大减少
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        set_ = set()
        res = [0, 0]
        for num in nums:
            if num not in set_:
                set_.add(num)
            else:
                res[0] = num
        res[1] = (set(range(1, len(nums)+1)) - set_).pop()
        return res