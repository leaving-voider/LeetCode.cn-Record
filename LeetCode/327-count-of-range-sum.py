###############################################################################################
# 前缀和，不过超时，数据量太大，n到了10^5数量级，n^2算法确实超时
# 前缀和肯定免不了，所以只能剪枝，但由于数组不是有序的，也不能排序，剪不了
###########
# 时间复杂度：O(n^2)
# 空间复杂度：O(n)
###############################################################################################
class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        sums = [0]
        for num in nums:
            sums.append(sums[-1] + num)
        
        len_, res = len(nums), 0
        for i in range(1, len_+1):
            for j in range(i, len_+1):
                seg_sum = sums[j] - sums[i-1]
                if seg_sum >= lower and seg_sum <= upper:
                    res += 1
        return res

###############################################################################################
# 既然nums不能排序，没关系，反正我们枚举sums的每个j 和 i，但也不能直接对sums排序，因为 j 严格 大于 i才行
# 不然得到的前缀和是没意义的，那怎么保证 j 严格大于 i呢，归并排序！！！带入归并的是sums而不是nums，绝了
###########
# 时间复杂度：O(nlogn)
# 空间复杂度：O(n)
###############################################################################################
class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        def merge_sort(sums, l, r):
            if l >= r:
                x = sums[l] - sums[l-1]
                return int(x >= lower and x <= upper)
            
            mid, res = (l+r)>>1, 0
            res += merge_sort(sums, l, mid)
            res += merge_sort(sums, mid+1, r)

            # 这里可以说是吃尽了苦头，因为归并排序我传入的是1 ~ len(nums)，没包括0，但从前面的解法可以看到，sums中的数 j>=1 而 i-1得到0
            # 在下面虽然也是i-1到0了，但有问题，因为sum[0] == 0没加入排序，并不符合sums前半部分递增，需要单独处理sum[0]，在每个循环里也就是sums[l]
            for j in range(mid+1, r+1):
                res += 1 if sums[j] - sums[l-1] >= lower and sums[j] - sums[l-1] <= upper else 0
            a, b = mid+1, mid+1

            for i in range(l+1, mid+1):
                while a < r+1 and sums[a] - sums[i-1] < lower: # 这样出来a及其后面的去减nums[i]都大于等于lower
                    a += 1
                while b < r+1 and sums[b] - sums[i-1] <= upper: # 这样b之前(不含b)的减nums[i]都小于等于upper
                    b += 1

                # 这里不用做额外判断，如果a == r+1，b也必定==r+1，若a<r+1而b==r+1，还是一样的加上即可
                res += b - a # 加上 a 到 b-1之间的数量就行了，即b-1 - a + 1 = b - a

            i, j, c = l, mid+1, []
            while i<=mid and j<=r:
                if sums[i] <= sums[j]:
                    c.append(sums[i])
                    i += 1
                else:
                    c.append(sums[j])
                    j += 1
            
            if i<=mid:
                c.extend(sums[i:mid+1])
            if j<=r:
                c.extend(sums[j:r+1])
            sums[l:r+1] = [per for per in c]

            return res
        
        sums = [0]
        for num in nums:
            sums.append(sums[-1] + num)

        return merge_sort(sums, 1, len(nums))

# 这个更好，把sums[0]也加入排序，就没有上面的问题
class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        def merge_sort(sums, l, r):
            if l >= r: # 单个的就不用加了，已经被计算过了
                return 0
            
            mid, res = (l+r)>>1, 0
            res += merge_sort(sums, l, mid)
            res += merge_sort(sums, mid+1, r)

            a, b = mid+1, mid+1
            for i in range(l, mid+1):
                while a < r+1 and sums[a] - sums[i] < lower: # 这样出来a及其后面的去减nums[i]都大于等于lower
                    a += 1
                while b < r+1 and sums[b] - sums[i] <= upper: # 这样b之前(不含b)的减nums[i]都小于等于upper
                    b += 1

                # 这里不用做额外判断，如果a == r+1，b也必定==r+1，若a<r+1而b==r+1，还是一样的加上即可
                res += b - a # 加上 a 到 b-1之间的数量就行了，即b-1 - a + 1 = b - a

            i, j, c = l, mid+1, []
            while i<=mid and j<=r:
                if sums[i] <= sums[j]:
                    c.append(sums[i])
                    i += 1
                else:
                    c.append(sums[j])
                    j += 1
            
            if i<=mid:
                c.extend(sums[i:mid+1])
            if j<=r:
                c.extend(sums[j:r+1])
            sums[l:r+1] = [per for per in c]

            return res
        
        sums = [0]
        for num in nums:
            sums.append(sums[-1] + num)

        return merge_sort(sums, 0, len(nums))