###############################################################################################
# 哈希 + 贪心 + 二分
###########
# 时间复杂度：O(n + mlogm)，遍历target + 求最长递增子序列，n为target长度，m为arr长度
# 空间复杂度：O(n)，哈希表 + 最长序列空间消耗，都是O(n)的
###############################################################################################
class Solution:
    def minOperations(self, target: List[int], arr: List[int]) -> int:
        dict_ = defaultdict(int)
        for i in range(len(target)):
            dict_[target[i]] = i 
        
        u = []
        for i in range(len(arr)):
            if arr[i] in dict_:
                u.append(dict_[arr[i]])
        if not len(u):
            return len(target) 
        
        longest = [u[0]] # 当前最长
        for i in range(1, len(u)):
            if u[i] > longest[-1]:
                longest.append(u[i])
            else:
                l, r = 0, len(longest) - 1
                while l < r:
                    mid = (l+r+1)//2
                    if longest[mid] < u[i]:
                        l = mid 
                    else:
                        r = mid - 1
                longest[l+1 if longest[l] < u[i] else l] = u[i] # 这种改值操作，不会改变原来已经找到的最长递增子序列的长度
        return len(target) - len(longest)