###############################################################################################
# 自己解：利用异或性质，加上一部分额外空间开销，减少异或的大量计算量，但三重循环仍然太耗时
###########
# 时间复杂度：O(n^3)
# 空间复杂度：O(n)，cals数组开销
###############################################################################################
class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        cals = [0]
        for per in arr:
            cals.append(cals[-1]^per)
        n = len(arr)
        nums = 0
        for i in range(0, n-1):
            for j in range(i+1, n):
                for k in range(j, n):
                    # if cals[i]^cals[j] == cals[j]^cals[k+1]: # 根据官方的解，这一步可以进一步优化：判断两边是否相等，那么利用异或性质，可约掉cals[j]
                    if cals[i] == cals[k+1]: # 少了异或运算，完成时间少一倍
                        nums += 1
        return nums

###############################################################################################
# 官方给的进一步优化，基于前面约掉了cals[j]，说明这个j已经不重要了，但凡满足cals[i] == cals[k+1]
# j为中间的任何值都可以，那么直接去掉j那个循环，变成二重循环，但是由于在j循环中每次都加了1，因此这个
# nums在去掉一个循环后，需要加上j循环的所有可行的数量
###########
# 时间复杂度：O(n^2)
# 空间复杂度：O(n)，cals数组开销
###############################################################################################
class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        cals = [0]
        for per in arr:
            cals.append(cals[-1]^per)
        n = len(arr)
        nums = 0
        for i in range(0, n-1):
            for k in range(i+1, n):
                if cals[i] == cals[k+1]:
                    nums += (k - i) # 一次性加上全部j的可行解
        return nums



###############################################################################################
# 再进一步优化，利用哈希表（这里就是Counter类）的性质，大大减少查询时间，可忽略不计，则整个优化为一重循环
# 该方法很巧妙，能利用哈希表的地方，基本都能让原来的时间复杂度降一个n倍
# 值得注意的是，在循环里先计数cals[k]以及序号，和先判断cals[k + 1] in cnt的顺序是没有关系的
# 原因是cals[k]和cals[k+1]当且仅当一种情况会是相等的，即第k+1个数为0，才可能cals[k+1] = cals[k]^0 = cals[k]
# 但题目明确指定，每个数必定大于等于1
###########
# 时间复杂度：O(n)
# 空间复杂度：O(n)，cals数组开销，以及两个哈希表
###############################################################################################
class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        cals = [0]
        for per in arr:
            cals.append(cals[-1]^per)
        n = len(arr)

        cnt, total = Counter(), Counter()
        ans = 0
        for k in range(n):
            cnt[cals[k]] += 1 # 记录前面相同cals值的个数，可能有多个
            total[cals[k]] += k # 记录那个序号，其实相当于i，便于后面 k - i 操作，只不过i一直在叠加，而k也按相同的个数来翻倍 
            if cals[k + 1] in cnt: # 这个其实就是判断了是否有cals[i] 和 现在的cals[k+1]相等
                ans += cnt[cals[k + 1]] * k - total[cals[k + 1]]

        return ans


###############################################################################################
# 再最后优化一点。。。官方利用python3.8的新语法，海象运算符:=，让我们能够仅遍历一次arr数组
# 不过正如前面一个优化中我分析的一样，判断和赋值的顺序可变，因此改了下，不需要新的运算符了
# 代码至此非常简洁。。。
###########
# 时间复杂度：O(n)，其中 n 是数组 arr 的长度
# 空间复杂度：O(n)，cals数组开销，以及两个哈希表
###############################################################################################
class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        cnt, total = Counter(), Counter()
        ans = calsInc = 0
        for k in range(len(arr)):
            cnt[calsInc] += 1
            total[calsInc] += k
            calsInc ^= arr[k]
            if calsInc in cnt:
                ans += cnt[calsInc] * k - total[calsInc]
        return ans