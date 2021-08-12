###############################################################################################
# 堆排序 + 堆优化，虽然排序只需要O(n), 但后面遍历的时间复杂度超过O(n)
###########
# 时间复杂度：O(nlogn)，因为每次pop最小元素就需要down
# 空间复杂度：O(n)
###############################################################################################
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        heap, size = [0] + [num for num in nums], len(nums)
        def down(x):
            t = x
            if x*2 <= size and heap[x*2] < heap[t]:
                t = x*2
            if x*2+1 <= size and heap[x*2+1] < heap[t]:
                t = x*2+1
            if t != x:
                heap[x], heap[t] = heap[t], heap[x]
                down(t)
        for i in range(size//2, 0, -1): # 堆排序 O(n)
            down(i)
        
        res = sec = 0
        last = None
        for _ in range(size):
            if heap[1] - 1 == last or heap[1] == last: # 重复元素没有任何帮助
                if heap[1] != last:
                    sec += 1
                    last = heap[1]
            else:
                res = max(res, sec)
                last = heap[1]
                sec = 1
            heap[1], heap[size] = heap[size], heap[1]
            size -= 1
            down(1)
        res = max(res, sec)
        return res


# 改成了一遍遍历，利用哈希表查找下一个在不在，然后每次遍历不是重复遍历，我们只从每个序列最小的开始遍历（即不存在num-1）
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sets = set(nums)
        res = 0
        for num in sets: # 且只需要遍历集合里的数就可以了，因为重复的数没必要遍历
            if num - 1 not in sets: # 我们只枚举起点（从最小的开始）
                i = num
                while i + 1 in sets:
                    i += 1
                res = max(res, i - num + 1)
        return res