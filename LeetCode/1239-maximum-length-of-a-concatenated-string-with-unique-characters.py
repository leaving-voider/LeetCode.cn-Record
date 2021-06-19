###############################################################################################
# 官方方法，利用位运算，删除一些内部有重复字母的串，再递归遍历所有情况
###########
# 时间复杂度：O(∣Σ∣ + 2^n)，遍历所有字符串需要 O(∣Σ∣), 回溯时由于每个元素有选或不选两种情况, 共2^n种组合方式
# 空间复杂度：O(n)，递归消耗
###############################################################################################
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        masks = []
        for per in arr:
            mask = 0
            for ch in per:
                index = ord(ch) - ord("a")
                if((mask >> index) & 1): # 表示有重复的字母了
                    mask = 0
                    break
                mask |= (1 << index)
            if mask > 0: # 表示该串不含重复字母
                masks.append(mask)
        
        ans = 0
        def backtrack(pos: int, mask: int) -> None:
            if pos == len(masks): # 已经到了最后一层
                nonlocal ans # 标识该变量是上一级函数中的局部变量
                ans = max(ans, bin(mask).count("1")) # 数其二进制中有多少个1
                return
            
            if (mask & masks[pos]) == 0:   # mask 和 masks[pos] 无公共元素，其实这种判断算是一种剪枝
                backtrack(pos + 1, mask | masks[pos])
            # 还是需要试试不加的情况
            backtrack(pos + 1, mask)
        
        backtrack(0, 0)
        return ans

## 利用set替代检查重复的操作，实测时间消耗更少
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        masks = []
        for per in arr:
            mask = 0
            for ch in per:
                mask |= (1 << (ord(ch) - ord("a")))
            if len(per) == len(set(per)):
                masks.append(mask)
        
        ans = 0
        def backtrack(pos: int, mask: int) -> None:
            if pos == len(masks): # 已经到了最后一层
                nonlocal ans # 标识该变量是上一级函数中的局部变量
                ans = max(ans, bin(mask).count("1")) # 数其二进制中有多少个1
                return
            
            if (mask & masks[pos]) == 0:   # mask 和 masks[pos] 无公共元素，其实这种判断算是一种剪枝
                backtrack(pos + 1, mask | masks[pos])
            # 还是需要试试不加的情况
            backtrack(pos + 1, mask)
        
        backtrack(0, 0)
        return ans


###############################################################################################
# 官方方法，将上面的递归转化为迭代，减少时间消耗，增加空间消耗
###########
# 时间复杂度：O(∣Σ∣ + 2^n)，遍历所有字符串需要 O(∣Σ∣), 每次遍历masks的长度都会倍增，最坏还是2^n消耗
# 空间复杂度：O(2^n)，masks数组空间消耗
###############################################################################################
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        masks = [0] # 初始化一个没加任何串的情况
        ans = 0
        for per in arr:
            if len(per) != len(set(per)):
                continue
            mask = 0
            for ch in per:
                mask |= (1 << (ord(ch) - ord("a")))

            for i in range(len(masks)):
                m = masks[i]
                if m & mask == 0: # 无公共元素
                    masks.append(m | mask)
                    ans = max(ans, bin(masks[-1]).count("1"))
        return ans


###############################################################################################
# 参考其他人的方法，使用动规方法
###########
# 时间复杂度：O(n + 递归找最优消耗)，实测证明时间消耗非常小，超过100%的用户
# 空间复杂度：O(n)，动规数组
###############################################################################################
class Solution:
    def overlap(self, s1, s2):
        return len(s1+s2) != len(set(s1+s2))

    def self_overlap(self, s):
        return len(s) != len(set(s))

    def max_substring(self, arr) -> str:
        len_ = len(arr)
        dp = [""]*(len_+1)

        for i in range(1, len_+1):
            if self.self_overlap(arr[i-1]): # 第i个串自己有重复
                dp[i] = dp[i-1]
            elif not self.overlap(dp[i-1], arr[i-1]): # 第i个串和前面的最长串无交集
                dp[i] = dp[i-1] + arr[i-1]
            else:
                # 第i个串和前面的最长串无交集
                no_arr_i = []
                for j in range(1, i):
                    if not self.overlap(arr[j-1], arr[i-1]): # 把前i个(不含i)所有和第i个串无交集的取出来
                        no_arr_i.append(arr[j-1])
                # 单独计算这些串中最长的可行解，并加上第i个串
                max_arr_i = arr[i-1] if len(no_arr_i) == 0 else self.max_substring(no_arr_i)+arr[i-1]
                # 如果比不加第i个串的情况更好，则加上
                dp[i] = max_arr_i if len(max_arr_i) > len(dp[i-1]) else dp[i-1]
        return dp[len_]

    def maxLength(self, arr: List[str]) -> int:  
        return len(self.max_substring(arr))

## 进行我最擅长的空间优化，至此代码较为精简美观
class Solution:
    def max_substring(self, arr) -> str:
        dp = ""
        for i, s in enumerate(arr):
            if len(s) != len(set(s)): # 第i个串自己有重复
                continue
            elif len(dp+s) == len(set(dp+s)): # 第i个串和前面的最长串无交集
                dp += s
            else: # 第i个串和前面的最长串无交集
                # 把前i个(不含i)所有和第i个串无交集的取出来
                no_arr_i = [arr[j] for j in range(i) if len(arr[j]+s) == len(set(arr[j]+s))]
                # 单独计算这些串中最长的可行解，并加上第i个串
                max_arr_i = s if len(no_arr_i) == 0 else self.max_substring(no_arr_i)+s
                # 如果比不加第i个串的情况更好，则加上
                dp = max_arr_i if len(max_arr_i) > len(dp) else dp
        return dp

    def maxLength(self, arr: List[str]) -> int:  
        return len(self.max_substring(arr))