###############################################################################################
# 利用字典树，官方给的离线询问+字典树，离线表示要先对nums和查询数组queries进行排序
###########
# 时间复杂度：O(NlogN+QlogQ+(N+Q)⋅L)，排序 nums 的时间复杂度为 O(NlogN)，N为nums长度，排序 queries 的时间复杂度为 O(QlogQ)
# Q为queries长度，插入和查询的时间复杂度为L（30个比特位）
# 空间复杂度：O(Q+N⋅L)，Q为用于存储排序后的查询数组中的查询在排序前数组中的位置，字典树的最坏开销为O(N⋅L)，即每个数都开了L个节点
###############################################################################################
class Trie:
    L = 30

    def __init__(self):
        self.left = None # 代表0
        self.right = None # 代表1

    def insert(self, val: int):
        node = self
        for i in range(Trie.L-1, -1, -1): # 官方给的从30开始，本人分析后将其改成29
            bit = (val >> i) & 1
            if bit == 0:
                if not node.left:
                    node.left = Trie()
                node = node.left
            else:
                if not node.right:
                    node.right = Trie()
                node = node.right
    
    def getMaxXor(self, val: int) -> int:
        ans, node = 0, self
        for i in range(Trie.L-1, -1, -1):
            bit = (val >> i) & 1
            check = False # 表示该bit位是否找到了相反的
            if bit == 0:
                if node.right:
                    node = node.right
                    check = True
                else:
                    node = node.left
            else:
                if node.left:
                    node = node.left
                    check = True
                else:
                    node = node.right
            if check: # 找到了，那么这一bit的异或则为1，若没找到那这一位默认为0
                ans |= 1 << i
        return ans


class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n, q = len(nums), len(queries)
        # 排序
        nums.sort()
        queries = sorted([(x, m, i) for i, (x, m) in enumerate(queries)], key=lambda query: query[1])
        
        ans = [0] * q
        t = Trie()
        idx = 0
        for x, m, qid in queries:
        	# 插入的都是小于本次的m的数
            while idx < n and nums[idx] <= m:
                t.insert(nums[idx])
                idx += 1
            if idx == 0:
                # 字典树为空
                ans[qid] = -1
            else:
                ans[qid] = t.getMaxXor(x)
        
        return ans

###############################################################################################
# 优化，官方给的在线询问 + 字典树，不用再排序了，分析可得有更小的时间和空间复杂度，但实际运行情况并非如此
# 原因未知。。
###########
# 时间复杂度：O((N+Q)⋅L)，插入和查询的时间复杂度为L（30个比特位）
# 空间复杂度：O(N⋅L)，字典树的最坏开销为O(N⋅L)，即每个数都开了L个节点
###############################################################################################
class Trie:
    L = 30

    def __init__(self):
        self.left = None # 代表0
        self.right = None # 代表1
        self.minValue = float("inf")

    def insert(self, val: int):
        node = self
        node.minValue = min(node.minValue, val)
        for i in range(Trie.L-1, -1, -1): # 官方给的从30开始，本人分析后将其改成29
            bit = (val >> i) & 1
            if bit == 0:
                if not node.left:
                    node.left = Trie()
                node = node.left
            else:
                if not node.right:
                    node.right = Trie()
                node = node.right
            node.minValue = min(node.minValue, val)
    
    def getMaxXorWithLimit(self, val: int, limit: int) -> int:
        ans, node = 0, self
        # 没有一个数小于这个limit，直接返回-1
        if node.minValue > limit:
        	return -1
        for i in range(Trie.L-1, -1, -1):
            bit = (val >> i) & 1
            check = False # 表示该bit位是否找到了相反的
            if bit == 0:
                if node.right and node.right.minValue <= limit: # 加了个条件，有小于limit才进入
                    node = node.right
                    check = True
                else:
                    node = node.left
            else:
                if node.left and node.left.minValue <= limit:
                    node = node.left
                    check = True
                else:
                    node = node.right
            if check: # 找到了，那么这一bit的异或则为1，若没找到那这一位默认为0
                ans |= 1 << i
        return ans


class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        q = len(queries)
        t = Trie()
        for num in nums:
            t.insert(num)

        ans = [0] * q
        for i, (x, m) in enumerate(queries):
            ans[i] = t.getMaxXorWithLimit(x, m)
        
        return ans