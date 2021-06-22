###############################################################################################
# 使用【31. 下一个排列的官方题解】中的下一个排列方法
###########
# 时间复杂度：O(n*n!), n为数组长，每次调用 next_permutation 最多扫描两次，反转一次；排列共n!种，第一次sorted排序O(nlogn)，忽略不计
# 空间复杂度：O(1)，返回值不计入消耗
###############################################################################################
class Solution:
    def next_permutation(self, s: str) -> List[str]:
        i = len(s) - 2
        while i>=0 and s[i] >= s[i+1]:
            i -= 1
        if i >= 0:
            j = len(s) - 1
            while i <= j and s[i] >= s[j]:
                j -= 1
            s[i], s[j] = s[j], s[i]

        left, right = i+1, len(s)-1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return s
        
    def permutation(self, s: str) -> List[str]:
        s = sorted(s)
        res = []
        while(len(s) > 0):
            s = ''.join(self.next_permutation(list(s)))
            if s not in res:
                res.append(s)
            else:
                break
        return res

## 稍微根据python语法和此题对next_permutation的具体使用，精简了下代码，算法本质没变
class Solution:
    def next_permutation(self, s: str) -> List[str]:
        for i in range(len(s)-2, -2, -1):
            if s[i] < s[i+1] and i >= 0:
                j = next(j for j in range(len(s)-1, i, -1) if s[j]>s[i])
                s[i], s[j] = s[j], s[i]
                break
        s[i+1:] = s[i+1:][::-1]
        return s
        
    def permutation(self, s: str) -> List[str]:
        s = sorted(s)
        res = []
        while True:
            s = ''.join(self.next_permutation(list(s)))
            if s not in res:
                res.append(s)
            else:
                break
        return res